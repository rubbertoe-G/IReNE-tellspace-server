from flask import current_app, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, \
    jwt_required, get_jwt_identity, get_raw_jwt
from google.oauth2 import id_token
from google.auth.transport import requests

from utils.responses import ApiResult, ApiException
from utils.exceptions import TellSpaceAuthError

from cachetools import TTLCache

from datetime import timedelta

from daos.dao_TS import *

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Set blacklist set for blacklisted tokens
# TODO: Replace blacklist with a Redis Store
# Set tll to the same time of the ttl of the token #
blacklist = TTLCache(maxsize=10000, ttl=120)


@current_app.jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """Verifies if a token has been blacklisted."""
    jti = decrypted_token['jti']
    if blacklist.currsize == 0:
        return False
    entry = blacklist.get(jti)  #search for the jti on the blacklist#
    return entry

@bp.route("/<google_token>", methods=['GET'])
def verify_google(google_token: str):

    print(google_token)


    id_info = id_token.verify_oauth2_token(
        google_token,
        requests.Request(),
        current_app.config['GOOGLE_OAUTH_CLIENT_ID'])

    return id_info



@bp.route('/me', methods=['GET'])
@jwt_required
def auth_me():
    """"Return the user information from the database."""
    # TODO: Use DAOs to look for user in the database.
    email = get_jwt_identity()
    user = get_me(email)

    if user.approved and (not user.banned):
        return ApiResult(
            id=user.id.__str__(),
            first_name=user.first_name,
            last_name=user.email,
            email=user.email,
            faculty=user.faculty
        )

    raise TellSpaceAuthError(msg="Access denied. User is not approved or is banned.")


@bp.route('/refresh', methods=["GET"])
@jwt_refresh_token_required
def auth_refresh():
    """Return a new access_token given a valid refresh token."""
    email = get_jwt_identity()
    access_token = create_access_token(identity=email, expires_delta=timedelta(hours=2))
    return ApiResult(access_token=access_token)


@bp.route("/logout")
@jwt_required
def auth_logout():
    """Revoke the Google authorization and add tokens to blacklist"""
    jti = get_raw_jwt()['jti']
    blacklist[jti] = True   # Add the jti to the cache with value true #
    return ApiResult(message="Successfully logged out.")