from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.db.model import MotModel  # Unused import to make flask_migrate work

app = Flask(__name__)


def main():
    with app.app_context():
        # DATABASE CONFIGURATION
        app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        sa.init_app(app)

        # ----------------------------------------------------------------------
        # CORS CONFIGURATION
        # ----------------------------------------------------------------------
        CORS(app, resources={
            '/*': {
                'allow_headers': [
                    'accept',
                    'accept-encoding',
                    'authorization',
                    'content-type'
                ],
                'methods': [
                    'delete',
                    'get',
                    'post',
                    'patch',
                    'put',
                    'options'
                ],
                'origins': [
                    'http://localhost:8000',
                    'http://localhost:3000',
                ]
            }
        })
        migration = Migrate(app, sa)

    return app
