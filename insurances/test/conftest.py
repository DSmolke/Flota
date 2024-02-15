import pytest
import logging

from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api

from app.env_variables import TEST_SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa

from app.route.insurance import AllInsurancesResource, InsurancesResource, InsuranceResourceAdd

logging.basicConfig(level=logging.INFO)

@pytest.fixture()
def app():
    """
    Create and configure the Flask application.

    :return: The Test Flask application instance.

    """
    app = Flask(__name__)

    with app.app_context():
        app.config.update({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': TEST_SQLALCHEMY_DATABASE_URI,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False})

        logging.info(TEST_SQLALCHEMY_DATABASE_URI)

        sa.init_app(app)

        sa.drop_all()
        sa.create_all()


        api = Api(app)
        api.add_resource(AllInsurancesResource, '/insurances/all')
        api.add_resource(InsurancesResource, '/insurances/<int:insurance_id>')
        api.add_resource(InsuranceResourceAdd, '/insurances')

    yield app

@pytest.fixture()
def client(app) -> FlaskClient:
    """
    .. py:function:: client(app) -> FlaskClient

       This method creates a Flask test client for the given Flask app.

       :param app: The Flask app object.
       :type app: flask.Flask
       :return: The Flask test client.
       :rtype: flask.testing.FlaskClient

       Example usage:

       .. code-block:: python

          app = create_app()
          test_client = client(app)
    """
    client: FlaskClient = app.test_client()
    return client


@pytest.fixture()
def sqlalchemy_database_uri():
    """
    Returns the SQLAlchemy database URI.

    :return: The SQLAlchemy database URI as a string.
    """
    return SQLALCHEMY_DATABASE_URI


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    pass


@pytest.fixture()
def insurance_data():
    """
    This method returns a dictionary representing insurance data.

    :return: A dictionary containing the following keys:
        - 'legal_identifier': A string representing the legal identifier for the insurance.
        - 'start_date': A string representing the start date of the insurance.
        - 'end_date': A string representing the end date of the insurance.
        - 'car_registration_number': A string representing the car registration number associated with the insurance.
        - 'img_url': A string representing the URL of an image related to the insurance.
        - 'active': A boolean indicating whether the insurance is active or not.
    """
    return {
        "legal_identifier": "KPA111111111111",
        "start_date": "2022-01-01",
        "end_date": "2023-01-01",
        "car_registration_number": "DPL96RR",
        "img_url": "https://amazon.com",
        "active": True
    }