from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.db.model import MotModel  # Unused import to make flask_migrate work
from app.route.mot import AllMotsResource, MotsResource, MotResourceAdd

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

        # ----------------------------------------------------------------------
        # API CONFIGURATION
        # ----------------------------------------------------------------------
        api = Api(app)
        api.add_resource(AllMotsResource, '/mots/all')
        api.add_resource(MotsResource, '/mots/<int:mot_id>')
        api.add_resource(MotResourceAdd, '/mots')

    return app
