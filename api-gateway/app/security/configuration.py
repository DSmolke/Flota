import jwt
import logging

from functools import wraps
from flask import request, make_response
from datetime import datetime, timedelta

from app.env_variables import JWT_AUTHMAXAGE, JWT_SECRET, JWT_PREFIX, JWT_AUTHTYPE, JWT_REFRESHMAXAGE
from app.db.model import UserModel
logger = logging.getLogger(__name__)

# ------------------------------------------------------------
# Security configuration
# ------------------------------------------------------------

def configure_security(app):
    # --------------------------------------------------------
    # Logging in
    # --------------------------------------------------------
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = UserModel.find_by_username(username)

        if not user:
            return make_response({'message': 'Authentication failed [1] !'}, 400)

        if not user.active:
            return make_response({'message': 'Authentication failed [2] !'}, 500)

        if not user.check_password(password):
            return make_response({'message': 'Authentication failed [3] !'}, 400)

        access_token_exp = int((datetime.utcnow() + timedelta(minutes=JWT_AUTHMAXAGE)).timestamp())
        refresh_token_exp = int((datetime.utcnow() + timedelta(minutes=JWT_REFRESHMAXAGE)).timestamp())

        access_token_payload = {
            'iat': datetime.utcnow(),
            'exp': access_token_exp,
            'sub': user.id,
            'role': user.role
        }

        refresh_token_payload = {
            'iat': datetime.utcnow(),
            'exp': refresh_token_exp,
            'sub': user.id,
            'role': user.role,
            'access_token_exp': access_token_exp
        }

        access_token = jwt.encode(access_token_payload, JWT_SECRET, algorithm=JWT_AUTHTYPE)
        refresh_token = jwt.encode(refresh_token_payload, JWT_SECRET, algorithm=JWT_AUTHTYPE)


        response_body = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

        response = make_response(response_body, 201)
        response.set_cookie(key='access_token', value=access_token, httponly=True, secure=True)
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, secure=True)

        return response

    # --------------------------------------------------------
    # Refresh tokens
    # --------------------------------------------------------
    @app.route('/refresh', methods=['POST'])
    def refresh():

        request_data = request.get_json()
        refresh_token = request_data.get('refresh_token', '')
        # refresh_token = request.cookies['refresh_token']

        try:
            decoded_refresh_token = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_AUTHTYPE])
            new_access_token_exp = int((datetime.utcnow() + timedelta(minutes=JWT_AUTHMAXAGE)).timestamp())

            access_token_payload = {
                'iat': datetime.utcnow(),
                'exp': new_access_token_exp,
                'sub': decoded_refresh_token['sub'],
                'role': decoded_refresh_token['role']
            }

            refresh_token_payload = {
                'iat': datetime.utcnow(),
                'exp': decoded_refresh_token['exp'],
                'sub': decoded_refresh_token['sub'],
                'role': decoded_refresh_token['role'],
                'access_token_exp': new_access_token_exp
            }

            access_token = jwt.encode(access_token_payload, JWT_SECRET, algorithm=JWT_AUTHTYPE)
            refresh_token = jwt.encode(refresh_token_payload, JWT_SECRET, algorithm=JWT_AUTHTYPE)

            response_body = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

            response = make_response(response_body, 201)
            response.set_cookie('access_token', access_token)
            response.set_cookie('refresh_token', refresh_token)
            return response

        except Exception:
            return {"message": "Signature has expired"}, 403,  {'Content-Type': 'application/json'}


# --------------------------------------------------------------------------------------
# Authorization decorator
# --------------------------------------------------------------------------------------

def token_required(roles: list[str]):
    """
    Checks if:
    - access token is valid
    - user has role that is required
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):

            header = request.headers.get('Authorization')

            if not header:
                return make_response({'message': 'Authorization failed [1] !'}, 401)

            if not header.startswith(JWT_PREFIX):
                return make_response({'message': 'Authorization failed [2] !'}, 401)

            access_token = header.split(' ')[1]

            try:
                access_token_data = jwt.decode(access_token, JWT_SECRET, algorithms=[JWT_AUTHTYPE])

                if access_token_data['role'].lower() not in [role.lower() for role in roles]:
                    return make_response({'message': 'Acess denied [1]!'}, 403)

                if datetime.fromtimestamp(access_token_data['exp']) < datetime.utcnow():
                    return make_response({'message': 'Acess denied [2]!'}, 403)

            except Exception:
                return make_response({'message': 'Authorization failed [3] !'}, 403)

            return f(*args, **kwargs)

        return decorated

    return decorator

"""
Flow security jest następujące:
- gdy wejdziemy w /login, to sprawdzane jest czy [użytkownik istnieje, jest aktywny, czy hasło się zgadza],
jeżeli warunki są spełnione to zwracane są access i refresh tokeny w body, oraz w cookies

-gdy wejdziemy w /refresh, to dekodujemy refresh token, jeżeli jego 'exp' jest w przeszłości to rzucany jest wyjątek
jeżeli nie ma wyjątku, to tworzony jest nowy acces token, a refresh token dostaje ten sam 'exp', więc jak go przekroczy
to trzeba będzie się zalogować
"""

