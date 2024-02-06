from dotenv import load_dotenv
from pathlib import Path
from os import getenv
import logging

logger = logging.getLogger(__name__)

ENV_FILENAME = '.env'
ENV_PATH = Path.cwd().absolute().joinpath(f'{ENV_FILENAME}') # webapp/.env
load_dotenv(ENV_PATH)

"""
Import of environment variables used for configurations
"""

# MYSQL DB
DB_USERNAME = getenv('DB_USERNAME', 'user')
DB_PASSWORD = getenv('DB_PASSWORD', 'user1234')
DB_PORT = getenv('DB_PORT', 3306)
DB_NAME = getenv('DB_NAME', 'db_1')
DB_CONTAINER = getenv('DB_CONTAINER', 'mysql')
SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_CONTAINER}:{DB_PORT}/{DB_NAME}'

# TEST MYSQL DB
TEST_DB_USERNAME = getenv('TEST_DB_USERNAME', 'user')
TEST_DB_PASSWORD = getenv('TEST_DB_PASSWORD', 'user1234')
TEST_DB_PORT = getenv('TEST_DB_PORT', 3306)
TEST_DB_NAME = getenv('TEST_DB_NAME', 'db_1')
TEST_DB_CONTAINER = getenv('TEST_DB_CONTAINER', 'mysql')
TEST_SQLALCHEMY_DATABASE_URI = f'mysql://{TEST_DB_USERNAME}:{TEST_DB_PASSWORD}@{TEST_DB_CONTAINER}:{TEST_DB_PORT}/{TEST_DB_NAME}'


# EMAIL
MAIL_USERNAME = getenv('MAIL_USERNAME', 'DEFAULT MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD', 'DEFAULT MAIL_PASSWORD')

# JWT
JWT_ISSUER = getenv('JWT_ISSUER', 'DEFAULT JWT_ISSUER')
JWT_AUTHTYPE = getenv('JWT_AUTHTYPE', 'DEFAULT JWT_AUTHTYPE')
JWT_SECRET = getenv('JWT_SECRET', 'DEFAULT JWT_SECRET')
JWT_AUTHMAXAGE = int(getenv('JWT_AUTHMAXAGE', 'DEFAULT JWT_AUTHMAXAGE'))
JWT_REFRESHMAXAGE = int(getenv('JWT_REFRESHMAXAGE', 'DEFAULT JWT_REFRESHMAXAGE'))
JWT_PREFIX = getenv('JWT_PREFIX', 'DEFAULT JWT_PREFIX')


