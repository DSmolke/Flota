from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from app.cors.configuration import CORS_CONFIG
from app.db.configuration import sa
from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.route.user import UserResource, UserActivationResource
from flask_cors import CORS

from app.security.configuration import configure_security
from app.email.configuration import MAIL_SETTINGS, MailSender

from app.route.car import cars_blueprint

app = Flask(__name__)


def main():
    with app.app_context():
        # KONFIGURACJA BAZY
        app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        sa.init_app(app)

        # KONFIGURACJA API
        api = Api(app)
        api.add_resource(UserResource, '/users')
        api.add_resource(UserActivationResource, '/users/activate')

        # ----------------------------------------------------------------------
        # EMAIL CONFIGURATION
        # ----------------------------------------------------------------------
        app.config.update(MAIL_SETTINGS)
        MailSender.init(app)  # MailSender tworzy sobie intancję mail -> Mail(app)

        # ----------------------------------------------------------------------
        # SECURITY CONFIGURATION
        # ----------------------------------------------------------------------
        configure_security(app)

        # ----------------------------------------------------------------------
        # MIGRATIONS
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
                    'http://localhost:3000'
                ]
            }
        })

        app.register_blueprint(cars_blueprint)

        @app.route('/')
        def index():
            return 'Index'

    return app
