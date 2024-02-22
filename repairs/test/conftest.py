import pytest
import logging

from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api

from app.env_variables import TEST_SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.db.model import RepairStatus
from app.routes.repair_resources import RepairEndPointsMapper

from app.routes.repair_blueprints import repairs


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

        sa.session.add_all([
            RepairStatus(name='started'),
            RepairStatus(name='pending'),
            RepairStatus(name='ready')

        ])
        sa.session.commit()

        api = Api(app)
        RepairEndPointsMapper(api).init_endpoints()
        app.register_blueprint(repairs)


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
def repair_data():
    """
    Returns a dictionary containing the repair data.

    :return: A dictionary with the following keys:
             - car_id: an integer representing the car ID.
             - repair_status: an integer representing the repair status.
             - repair_description: a string describing the repair.
             - approximate_duration: an integer representing the approximate duration of the repair.
             - start_date: a string representing the start date of the repair in the format "YYYY-MM-DD".
             - garage_name: a string representing the name of the garage.
             - garage_phone: a string representing the phone number of the garage.
    """
    return {
        "car_id": 1,
        "repair_status": 1,
        "repair_description": "Seasonal tyres change",
        "approximate_duration": 1,
        "start_date": "2024-02-19",
        "garage_name": "WWA Main Garage",
        "garage_phone": "570688764"
    }


@pytest.fixture()
def desired_response_data(repair_data):
    """Adds an 'id' key to the repair data and returns the modified dictionary.

    :param repair_data: A dictionary containing repair data.
    :return: A dictionary with the 'id' key added.
    """
    return {**repair_data, "id": 1}
