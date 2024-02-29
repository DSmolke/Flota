import logging
import pytest
from flask import Flask

from app.routes.cepik import Cepik

@pytest.fixture()
def app():
    """
    Create an `app` for the testing using the pytest fixture. The `app` is an instance of the Flask application and is prepared using the Flask framework. The `app` is registered with the
    * Cepik blueprint for testing purposes.

      :return: The `app` object

    """
    app = Flask(__name__)
    with app.app_context():
        app.register_blueprint(Cepik)

    # clean up / reset resources here

    yield app
@pytest.fixture()
def client(app):
    """
    Returns a test client for the given Flask application.

    :param app: The Flask application to create a test client for.
    :return: A test client for the given Flask application.
    """
    return app.test_client()