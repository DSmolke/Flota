import pytest
import logging

from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api

from app.env_variables import TEST_SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.routes.driver import DriverEndPointsMapper


@pytest.fixture()
def app():
    """
    The `app` method is a fixture that initializes and configures a Flask application for testing purposes.

    The method creates a Flask app instance, sets the necessary app context, and updates the app configuration for testing. It initializes the SQLAlchemy database by dropping and creating
    * all tables and inserts some initial data into the database.

    Additionally, it sets up an API instance and maps the repair endpoints using the `RepairEndPointsMapper` class. Lastly, it registers the `repairs` blueprint with the app.

    :return: The initialized Flask app instance.
    """
    app = Flask(__name__)

    with app.app_context():
        app.config.update({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': TEST_SQLALCHEMY_DATABASE_URI,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False})

        sa.init_app(app)

        sa.drop_all()
        sa.create_all()

        api = Api(app)
        DriverEndPointsMapper(api).init_endpoints()

    yield app


@pytest.fixture()
def client(app) -> FlaskClient:
    """
    :param app: Flask application instance.
    :return: FlaskClient instance for testing the application.
    """
    client: FlaskClient = app.test_client()
    return client


@pytest.fixture()
def sqlalchemy_database_uri():
    """
    Returns the SQLAlchemy database URI.

    :return: The SQLAlchemy database URI.
    """
    return SQLALCHEMY_DATABASE_URI


@pytest.fixture()
def driver_data():
    return {
        "first_name": "Damian",
        "last_name": "Smolczynski",
        "phone_number": "570688764",
        "email": "d.smolczynski1@gmail.com",
        "car_registration": "WZ275EL"
    }


@pytest.fixture()
def desired_response_data(driver_data):
    return {**driver_data, "id": 1}
