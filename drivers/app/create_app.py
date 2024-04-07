from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.routes.driver import DriverEndPointsMapper

app = Flask(__name__)


def main() -> Flask:
    # -------------------------------------------------------------
    # DATABASE CONFIGURATION
    # -------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    sa.init_app(app)

    # -------------------------------------------------------------
    # CORS CONFIGURATION
    # -------------------------------------------------------------
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
            ],
            'origins': [
                'http://localhost:8000',
                'http://localhost:80',
            ]
        }
    })

    # -------------------------------------------------------------
    # API AND ENDPOINTS CONFIG
    # -------------------------------------------------------------
    api = Api(app)
    DriverEndPointsMapper(api).init_endpoints()

    # -------------------------------------------------------------
    # MIGRATION CONFIGURATION
    # -------------------------------------------------------------
    Migrate(app, sa)

    return app
