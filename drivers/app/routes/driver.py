import logging

from flask import Response, make_response, request
from flask_restful import Resource, reqparse, Api
from sqlalchemy.exc import IntegrityError
from app.validator.driver import driver_schema
from app.db.model import DriverModel
from app.db.configuration import sa

logging.basicConfig(level=logging.INFO)


class AddDriverResource(Resource):
    """
    Resource for adding a new driver.

    :param Resource: The base resource class.
    :type Resource: class

    :ivar parser: RequestParser instance for parsing request data.
    :vartype parser: RequestParser

    """
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, required=True)
    parser.add_argument('last_name', type=str, required=True)
    parser.add_argument('phone_number', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('car_registration', type=str, required=True)

    def post(self) -> Response:
        """
        :post: Endpoint to create a new driver.

        :return: A tuple containing the driver data as a dictionary, the status code 201,
                 and the content type header as a dictionary, if the driver is successfully
                 created.

                 A dictionary containing the error message and the status code 403, if
                 the request fails due to an integrity error.

                 A dictionary containing the error message and the status code 400, if the
                 request is invalid or contains incorrect data types.
        """
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
    """
    A class representing the resource for retrieving all drivers.

    Methods:
        get() -> Response: Retrieve all drivers and return a response with the data.
    """
    def get(self) -> Response:
        """
        Get all drivers.

        :return: HTTP response object with JSON data and status code 200.
        :rtype: flask.Response
        """
        drivers = DriverModel.get_all()
        response = make_response({'all_drivers': drivers})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        return response

class DriversResource(Resource):
    """
    This class represents a resource for managing drivers.

    Methods:
    - get(driver_id: int) -> Response: Retrieves information about a specific driver.
    - delete(driver_id: int) -> Response: Deletes a specific driver.
    - patch(driver_id: int) -> Response: Updates information for a specific driver.

    """
    def get(self, driver_id: int) -> Response:
        """
        Get driver information by driver ID.

        :param driver_id: The ID of the driver.
        :type driver_id: int
        :return: The driver information as a dictionary and the response status code.
        :rtype: tuple(dict, int)
        """
        driver = DriverModel.get_by_id(driver_id)
        if driver:
            return driver.as_dict(), 200
        return {"message": "Driver does not exist"}, 404

    def delete(self, driver_id: int) -> Response:
        """
        Delete a driver by their ID.

        :param driver_id: The ID of the driver to be deleted.
        :return: A dictionary with a "message" key and a corresponding HTTP status code.
            - If the driver is found and successfully deleted, the message is "Driver has been deleted" and the status code is 200.
            - If the driver is not found, the message is "Driver not found" and the status code is 404.
        """
        driver_to_delete = DriverModel.get_by_id(driver_id)
        if driver_to_delete:
            driver_to_delete.delete()
            return {"message": "Driver has been deleted"}, 200
        return {"message": "Driver not found"}, 404

    def patch(self, driver_id: int) -> Response:
        """
        Update a driver record based on the provided driver ID.

        :param driver_id: The ID of the driver to update.
        :type driver_id: int
        :return: The updated driver record.
        :rtype: Response
        """
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
    """

    DriverEndPointsMapper

    Class responsible for mapping endpoints to routes for the driver resources.

    """
    endpoints_with_routes = [
        (AddDriverResource, '/driver'),
        (AllDriversResource, '/drivers/all'),
        (DriversResource, '/driver/<int:driver_id>')
    ]

    def __init__(self, api: Api):
        self.api = api

    def init_endpoints(self) -> None:
        """
        Initializes the endpoints by adding them to the API.

        :return: None
        """
        for endpoint in self.endpoints_with_routes:
            self.api.add_resource(endpoint[0], endpoint[1])
