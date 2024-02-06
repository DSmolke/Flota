from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate

from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.cors.configuration import CORS_CONFIG

from app.route.car import AllCarsResource, CarResource, CarResourceAdd

app = Flask(__name__)


def main():
    """
    The main() method is the entry point of the application. It sets up the database configuration, API configuration, and CORS configuration. It also returns the Flask application object
    *.

    :return: The Flask application object.

    Example Usage:

    ```python
    app = main()
    app.run()
    ```
    """
    with app.app_context():
        # DATABASE CONFIGURATION
        app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        sa.init_app(app)

        # API CONFIGURATION
        api = Api(app)
        api.add_resource(AllCarsResource, '/cars/all')
        api.add_resource(CarResource, '/car/<int:car_id>')
        api.add_resource(CarResourceAdd, '/car')

        # ----------------------------------------------------------------------
        # FLASK-MIGRATE CONFIGURATION
        # ----------------------------------------------------------------------
        migrate = Migrate(app, sa)

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

    return app
