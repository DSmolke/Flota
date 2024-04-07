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

# EMAIL
MAIL_USERNAME = getenv('MAIL_USERNAME', 'DEFAULT MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD', 'DEFAULT MAIL_PASSWORD')

