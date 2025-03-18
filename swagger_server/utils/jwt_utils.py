import jwt
import requests
from jwt import ExpiredSignatureError, InvalidTokenError
import json

from werkzeug.exceptions import Unauthorized

REGION = 'eu-central-1'
USER_POOL_ID = 'eu-central-1_FSieqcZdy'
APP_CLIENT_ID = '3icm227trvfbhbsar1vhtfe51p'
TOKEN_USE = 'id'

def verify_cognito_jwt(token):
    print("Hello world")
    # Construct issuer URL and JWKS URL
    issuer = f'https://cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}'
    jwks_url = f'{issuer}/.well-known/jwks.json'

    try:
        # Fetch JWKS keys
        response = requests.get(jwks_url)
        response.raise_for_status()
        jwks = response.json()
    except requests.exceptions.RequestException as e:
        raise Unauthorized from e

    try:
        # Extract header from token
        header = jwt.get_unverified_header(token)
    except jwt.DecodeError as e:
        raise Unauthorized from e

    # Find the key with matching kid
    kid = header.get('kid')
    if not kid:
        raise ValueError("Token header missing 'kid'")

    key = next((key for key in jwks['keys'] if key['kid'] == kid), None)
    if not key:
        raise Unauthorized

    try:
        # Convert JWK to RSA public key
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
    except (jwt.InvalidKeyError, ValueError) as e:
        raise Unauthorized from e

    try:
        # Verify token signature and claims
        decoded = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            issuer=issuer,
            audience=APP_CLIENT_ID,
            options={'verify_exp': True}
        )
    except ExpiredSignatureError as e:
        raise Unauthorized from e
    except InvalidTokenError as e:
        raise Unauthorized from e

    # Validate token use using the correct constant name
    if decoded.get('token_use') != TOKEN_USE:
        raise Unauthorized

    return decoded
