import logging

from flask import Flask, jsonify, Response, request
from app.service.models import CarDetails
from app.service.cepik_service import CepikSevice
from app.service.page_utils import map_report_result
from app.service.configuration import driver_linux

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def main():
    with app.app_context():

        @app.route('/car_status')
        def insurance_and_mot_details() -> Response:
            """
            :return: A JSON response containing insurance and MOT details for a given car.

            """
            data = request.get_json()
            try:
                car = CarDetails(data['registration'], data['vin'], data['first_registration_date'])
                res = map_report_result(CepikSevice(driver_linux, car_details=car).get_car_report())
                return jsonify(res)
            except Exception as e:
                return {'error': 'Invalid car details'}

        @app.route('/with_full_report_url')
        def get_full_report_url() -> Response:
            """
            Retrieves the full report URL for a given car using its registration, VIN, and first registration date.

            :return: a dictionary containing the car details and the full report URL
            """
            data = request.get_json()
            try:
                car = CarDetails(data['registration'], data['vin'], data['first_registration_date'])
                full_report_url = CepikSevice(driver_linux, car_details=car).get_full_vehicle_history_report_url()
                return {**car.as_dict(), 'full_report_url': full_report_url}

            except Exception as e:
                logging.info(e)
                return {'error': 'Invalid car details'}
    return app

