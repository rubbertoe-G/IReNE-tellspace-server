# TODO: Implement authentication strategy with flask dance and Google oAuth. Use decorators as needed.


from flask import current_app, jsonify
from flask_dance.contrib.google import make_google_blueprint, google
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, \
    jwt_required, get_jwt_identity, get_raw_jwt

from utils.responses import ApiResult, ApiException
from utils.exceptions import TellSpaceAuthError

from datetime import timedelta

from daos.dao_TS import *

import json

# Register Google oAuth Strategy blueprint
bp = make_google_blueprint(scope=["profile", "email"])
bp.url_prefix = "/"

# Set blacklist set for blacklisted tokens
# TODO: Replace blacklist with a Redis Store
token_blacklist = set()


@current_app.jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """Verifies if a token has been blacklisted."""
    jti = decrypted_token['jti']
    return jti in token_blacklist


@bp.route('/')
def auth_main():
    """Generate a new access token for the user. User must sign in to Google oAuth to get a valid token.
    """
    if not google.authorized:
        raise TellSpaceAuthError(msg="Client is not unauthorized. Please login at /google", status=401)

    # Get user email from Google Credentials to use as identity
    email = google.get("/oauth2/v2/userinfo").json()['email']

    # Get the user from the DB
    user = get_me(email)

    if user.approved:
        try:
            # Revoke Google Token. Login sequence requires user to sign in to google
            google_token = bp.token["access_token"]
            google.post(
                "https://accounts.google.com/o/oauth2/revoke",
                params={"token": google_token},
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            del bp.token
        except KeyError:
            raise TellSpaceAuthError(msg="No token to be revoked. Please login at /api/auth/login")

        # Use the email as the token identity
        return ApiResult(
            access_token=create_access_token(identity=email, expires_delta=timedelta(hours=1)),
            refresh_token=create_refresh_token(identity=email, expires_delta=timedelta(weeks=2))
        )

    raise TellSpaceAuthError(msg="This user has not been approved.")


@bp.route('/me')
@jwt_required
def auth_me():
    """"Return information from the database."""
    # TODO: Use DAOs to look for user in the database.
    email = get_jwt_identity()
    user = json.loads(get_me("asasdas").to_json())

    return ApiResult(response=user)


@bp.route('/refresh', methods=["GET"])
@jwt_refresh_token_required
def auth_refresh():
    """Return a new access_token given a valid refresh token."""
    email = get_jwt_identity()
    return ApiResult(access_token=create_access_token(identity=email, expires_delta=timedelta(hours=2)))


@bp.route("/logout")
@jwt_required
def auth_logout():
    """Revoke the Google authorization and add tokens to blacklist"""
    # Blacklist jwt tokens
    jti = get_raw_jwt()['jti']
    token_blacklist.add(jti)
    return ApiResult(message="Successfully logged out.")


