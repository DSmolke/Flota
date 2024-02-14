from os import getenv
from pathlib import Path
from dotenv import load_dotenv


ENV_FILENAME = '.env'
ENV_PATH = Path.cwd().absolute().joinpath(ENV_FILENAME)

# Code can also work without using .env due to native pipenv functionalities
load_dotenv(ENV_PATH)

"""
Import of environment variables used for configurations
"""

# AWS
AWS_ACCESS_KEY = getenv('AWS_ACCESS_KEY', 'DEFAULT AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY', 'DEFAULT AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = getenv('BUCKET_NAME', 'DEFAULT BUCKET_NAME')
BUCKET_SUBFOLDER_NAME = getenv('BUCKET_SUBFOLDER_NAME', 'DEFAULT BUCKET_SUBFOLDER_NAME')
