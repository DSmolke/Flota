import logging
from flask import Flask
from app.routes.cepik import Cepik

app = Flask(__name__)


def main():
    """
    Main Method

    This method initializes the application context and registers the Cepik blueprint. It then returns the application object.

    :return: The application object.
    """
    with app.app_context():
        app.register_blueprint(Cepik)

    return app

