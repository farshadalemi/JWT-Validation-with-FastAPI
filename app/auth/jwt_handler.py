import time
import jwt
from decouple import config

# The way that we map the .env config to variables in our logic(services)
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm ")


# It returns Generated Tokens (JWT)
def token_response(token: str):
    return{
        "access token" : token
    }

