import pytest
import logging

from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from flask_restful import Api

from app.env_variables import TEST_SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa

from app.route.mot import AllMotsResource, MotsResource, MotResourceAdd

logging.basicConfig(level=logging.INFO)

@pytest.fixture()
def app():
    """
    This method initializes and returns an instance of the Flask application with the necessary configurations and resources.

    :return: Flask application object
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
        api.add_resource(AllMotsResource, '/mots/all')
        api.add_resource(MotsResource, '/mots/<int:mot_id>')
        api.add_resource(MotResourceAdd, '/mots')

    yield app

@pytest.fixture()
def client(app) -> FlaskClient:
    """
    :param app: The Flask application instance.
    :return: A FlaskClient instance.

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
def mot_data():
    return {
        "legal_identifier": "XXX/XXX/XXX/XXXX/XXXX",
        "start_date": "2022-01-01",
        "end_date": "2023-01-01",
        "car_registration_number": "DPL96RR",
        "img_url": "https://amazon.com",
        "active": True
    }