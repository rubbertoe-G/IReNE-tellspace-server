from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")
PORT = os.getenv("PORT")

FLASK_DEBUG = os.getenv("FLASK_DEBUG")
DB = os.getenv("DB")


# Authorization
GOOGLE_OAUTH_CLIENT_ID="125759116505-flugvdnnv7lm6q6htj62uic5ut70e594.apps.googleusercontent.com"
GOOGLE_OAUTH_CLIENT_SECRET="eHJTs2-KrUEBiyXC9E5r1y3D"
OAUTHLIB_RELAX_TOKEN_SCOPE= True

# Set to TRUE for testing purpouses
OAUTHLIB_INSECURE_TRANSPORT= True
FLASK_SECRET_KEY="SuPeRsEcReTkEyThAtNoOnEcAnCrAcK"
FLASK_SALT="Justasaltysaltthatisverysalty"