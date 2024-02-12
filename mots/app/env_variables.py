from os import getenv
from pathlib import Path
from dotenv import load_dotenv


ENV_FILENAME = '.env'
ENV_PATH = Path.cwd().absolute().joinpath(ENV_FILENAME)

# Code can also work without using .env due to native pipenv functionalities
load_dotenv(ENV_PATH)

DB_USERNAME = getenv('DB_USERNAME', 'user')
DB_PASSWORD = getenv('DB_PASSWORD', 'user1234')
DB_PORT = getenv('DB_PORT', '3306')
DB_NAME = getenv('DB_NAME', 'db_1')
DB_CONTAINER = getenv('DB_CONTAINER', 'mysql')
SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_CONTAINER}:{DB_PORT}/{DB_NAME}'

TEST_DB_USERNAME = getenv('TEST_DB_USERNAME', 'user')
TEST_DB_PASSWORD = getenv('TEST_DB_PASSWORD', 'user1234')
TEST_DB_PORT = getenv('TEST_DB_PORT', '3306')
TEST_DB_NAME = getenv('TEST_DB_NAME', 'db_1')
TEST_DB_CONTAINER = getenv('TEST_DB_CONTAINER', 'mysql')
TEST_SQLALCHEMY_DATABASE_URI = f'mysql://{TEST_DB_USERNAME}:{TEST_DB_PASSWORD}@{TEST_DB_CONTAINER}:{TEST_DB_PORT}/{TEST_DB_NAME}'
