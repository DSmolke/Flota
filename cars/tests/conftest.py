import pytest
import logging

from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from flask_restful import Api

from app.env_variables import TEST_SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI
from app.db.configuration import sa
from app.db.model import FuelTypeModel, VehicleStatusModel
from app.route.car import AllCarsResource, CarResource, CarResourceAdd


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

        sa.init_app(app)

        sa.drop_all()
        sa.create_all()

        sa.session.add_all([
            FuelTypeModel(name='petrol', efficiency=0.89),
            FuelTypeModel(name='diesel', efficiency=0.95),
            FuelTypeModel(name='electric', efficiency=0.7),
            VehicleStatusModel(name='ready', description='Ready to use'),
            VehicleStatusModel(name='repair', description='Waiting for repairs to be done'),
            VehicleStatusModel(name='not_legal', description='Waiting for mot or insurance')
        ])
        sa.session.commit()

        api = Api(app)
        api.add_resource(AllCarsResource, '/cars/all')
        api.add_resource(CarResource, '/car/<int:car_id>')
        api.add_resource(CarResourceAdd, '/car')

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

@pytest.fixture()
def car_data():
    """
    Get car data.

    :return: A dictionary containing the car data with the following keys:
        - "registration": The registration number of the car.
        - "vin": The Vehicle Identification Number (VIN) of the car.
        - "make": The make of the car.
        - "model": The model of the car.
        - "first_registration_date": The date when the car was first registered.
        - "production_year": The year when the car was produced.
        - "mileage": The mileage of the car.
        - "fuel_consumption": The fuel consumption of the car.
        - "fuel_type_id": The ID of the fuel type of the car.
        - "vehicle_status_id": The ID of the vehicle status of the car.
    """
    return {
        "registration": "DPL96RR",
        "vin": "12AASL45J01234122",
        "make": "BMW",
        "model": "SERIES 3",
        "first_registration_date": "2024-01-04",
        "production_year": "2023",
        "mileage": "15000",
        "fuel_consumption": '6.99',
        "fuel_type_id": 1,
        "vehicle_status_id": 2
    }

@pytest.fixture()
def desired_response_data(car_data):
    """
    Creates the desired response data by adding an "id" key to the car_data dictionary.

    :param car_data: A dictionary containing car data.
    :return: The modified car_data dictionary with an additional "id" key.
    """
    return {**car_data, "id": 1}
