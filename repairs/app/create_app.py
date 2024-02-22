from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.db.model import RepairModel, RepairStatus # Models are imported and not used, but necessary for flask_migrate mechanizm
from app.db.configuration import sa
from app.routes.repair_resources import RepairEndPointsMapper
from app.routes.repair_blueprints import repairs

app = Flask(__name__)


def main() -> Flask:
    """
    Main Method

    Configures the Flask application and sets up the necessary components for the API.

    :return: The configured Flask application instance.
    :rtype: Flask
    """
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
    RepairEndPointsMapper(api).init_endpoints()
    app.register_blueprint(repairs)

    # -------------------------------------------------------------
    # MIGRATION CONFIGURATION
    # -------------------------------------------------------------
    Migrate(app, sa)

    return app
