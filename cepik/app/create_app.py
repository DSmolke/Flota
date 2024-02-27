from flask import Flask, jsonify, Response, request
from app.service.models import CarDetails
from app.service.cepik_service import CepikSevice
from app.service.page_utils import map_report_result
from app.service.configuration import driver_linux

app = Flask(__name__)


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

    return app

