import time
import jwt
from decouple import config

# The way that we map the .env config to variables in our logic(services)
JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


# It returns Generated Tokens (JWT)
def token_response(token: str):
    return{
        "access token" : token
    }

# It Sign the JWT str
def signJWT(userID: str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)
    return token_response(token)


# It returns the decoded token to be checked while user sends the req
def decodeJWT(token : str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm = JWT_ALGORITHM)
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}