from flask import Flask

from app.routes.cars import load_cars_data_blueprint
from app.routes.insurances import load_insurances_data_blueprint
from app.routes.mots import load_mots_data_blueprint

app = Flask(__name__)


def main():
    """
    Initializes the application and sets up the necessary configurations and resources.

    :return: The initialized Flask application.
    """
    with app.app_context():
        app.register_blueprint(load_cars_data_blueprint)
        app.register_blueprint(load_mots_data_blueprint)
        app.register_blueprint(load_insurances_data_blueprint)

    return app
