from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.db.model import InsuranceModel  # Unused import to make flask_migrate work
from app.route.insurance import AllInsurancesResource, InsurancesResource, InsuranceResourceAdd

app = Flask(__name__)


def main():
    """
    Initializes the application and sets up the necessary configurations and resources.

    :return: The initialized Flask application.
    """
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
                    'http://localhost:80',
                ]
            }
        })
        migration = Migrate(app, sa)

        # ----------------------------------------------------------------------
        # API CONFIGURATION
        # ----------------------------------------------------------------------
        api = Api(app)
        api.add_resource(AllInsurancesResource, '/insurances/all')
        api.add_resource(InsurancesResource, '/insurances/<int:insurance_id>')
        api.add_resource(InsuranceResourceAdd, '/insurances')

    return app
