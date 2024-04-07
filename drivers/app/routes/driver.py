import logging

from flask import Response, make_response, request
from flask_restful import Resource, reqparse, Api
from sqlalchemy.exc import IntegrityError
from app.validator.driver import driver_schema
from app.db.model import DriverModel
from app.db.configuration import sa

logging.basicConfig(level=logging.INFO)


class AddDriverResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, required=True)
    parser.add_argument('last_name', type=str, required=True)
    parser.add_argument('phone_number', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('car_registration', type=str, required=True)

    def post(self) -> Response:

        request_data = self.parser.parse_args()

        try:
            driver_schema.validate(request_data)
            driver = DriverModel(**request_data)
            driver.save()
            return driver.as_dict(), 201, {'Content-Type': 'application/json'}

        except IntegrityError as e:
            sa.session.rollback()
            return {"message": e.orig.args[1]}, 403

        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class AllDriversResource(Resource):

    def get(self) -> Response:

        drivers = DriverModel.get_all()
        response = make_response({'all_drivers': drivers})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        return response

class DriversResource(Resource):

    def get(self, driver_id: int) -> Response:

        driver = DriverModel.get_by_id(driver_id)
        if driver:
            return driver.as_dict(), 200
        return {"message": "Driver does not exist"}, 404

    def delete(self, driver_id: int) -> Response:

        driver_to_delete = DriverModel.get_by_id(driver_id)
        if driver_to_delete:
            driver_to_delete.delete()
            return {"message": "Driver has been deleted"}, 200
        return {"message": "Driver not found"}, 404

    def patch(self, driver_id: int) -> Response:

        try:
            data = request.get_json()
            driver_schema.validate(data)
            driver = DriverModel.get_by_id(driver_id)
            if driver:
                driver.update(data)
                return driver.as_dict(), 200
            return {"message": "Driver does not exist"}, 404
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class DriverEndPointsMapper:

    endpoints_with_routes = [
        (AddDriverResource, '/driver'),
        (AllDriversResource, '/drivers/all'),
        (DriversResource, '/driver/<int:driver_id>')
    ]

    def __init__(self, api: Api):
        self.api = api

    def init_endpoints(self) -> None:

        for endpoint in self.endpoints_with_routes:
            self.api.add_resource(endpoint[0], endpoint[1])
