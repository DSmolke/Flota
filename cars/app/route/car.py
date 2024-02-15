from flask_restful import Resource, reqparse
from flask import Response, make_response, request
from sqlalchemy.exc import IntegrityError

from app.db.configuration import sa
from app.db.model import CarModel
from app.validator.car import car_schema

import logging

logging.basicConfig(level=logging.DEBUG)


class AllCarsResource(Resource):
    """
    A class representing the resource for retrieving all cars.

    Methods:
        - get: Retrieves all cars and returns a JSON response.

    """
    def get(self) -> Response:
        """
        Get all cars.

        :return: Response object with a JSON containing all cars.
        """
        cars = CarModel.get_all()
        response = make_response({'all_cars': cars})
        response.headers['Content-Type'] = 'application/json'
        response.status = 200
        return response

class CarResource(Resource):
    """

    The `CarResource` class is a subclass of `Resource` and provides HTTP methods for interacting with car resources.

    It includes the following methods:

    - `get(self, car_id)`: Returns the details of a car with the given `car_id`. If the car exists, it returns the car details as a dictionary with a 200 status code. If the car does not
    * exist, it returns a 404 status code with a message indicating that the car does not exist.

    - `delete(self, car_id)`: Deletes the car with the given `car_id`. If the car exists, it deletes the car and returns a 200 status code with a message indicating that the car has been
    * deleted. If the car does not exist, it returns a 404 status code with a message indicating that the car was not found.

    - `patch(self, car_id)`: Updates the details of a car with the given `car_id` using the data provided in the request. First, it validates the request data using the `car_schema`. If
    * the validation succeeds, it retrieves the car with the given `car_id`, updates the car details with the request data, and returns the updated car details as a dictionary with a 200
    * status code. If the car does not exist, it returns a message indicating that the car does not exist.

    - The `patch()` method can raise a `ValueError` or `TypeError` if the request data is invalid. In this case, it returns a 400 status code with a message indicating that the request is
    * invalid.

    """
    def get(self, car_id) -> Response:
        """
        Retrieve a car by its ID.

        :param car_id: The ID of the car to retrieve.
        :return: A tuple consisting of the car dictionary and HTTP status code.
                 If the car is found, the car dictionary will be returned with a status code of 200 (OK).
                 If the car is not found, a dictionary with an error message will be returned with a status code of 404 (Not Found).
        """
        car = CarModel.get_by_id(car_id)
        if car:
            return car.as_dict(), 200
        return {"message": "Car does not exist"}, 404

    def delete(self, car_id) -> Response:
        """
        Delete a car by its ID.

        :param car_id: The ID of the car to be deleted.
        :return: A dictionary containing the message of the result and the HTTP status code.
        :rtype: Response
        :raises: None

        Example when one entry with id 1 is in the database:
            >>> delete(1)
            ({'message': 'Car has been deleted'}, 200)
            >>> delete(10)
            ({'message': 'Car not found'}, 404)
        """
        car_to_delete = CarModel.get_by_id(car_id)
        if car_to_delete:
            car_to_delete.delete()
            return {"message": "Car has been deleted"}, 200
        return {"message": "Car not found"}, 404

    def patch(self, car_id) -> Response:
        """
        Updates a car with the provided car_id.

        :param car_id: ID of the car to be updated.
        :return: Response containing the updated car details or an error message.
        """
        try:
            data = request.get_json()
            car_schema.validate(data)
            car = CarModel.get_by_id(car_id)
            if car:
                car.update(data)
                return car.as_dict(), 200
            return {"message": "Car does not exist"}, 404
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class CarResourceAdd(Resource):
    """
    :class:`CarResourceAdd` is a class that represents a resource for adding a car to a system.

    The class inherits from the `Resource` class.

    Attributes:
        parser (RequestParser): An instance of the `RequestParser` class used for parsing and validating request data.

    Methods:
        post(): Processes a POST request to add a car to the system.

    """
    parser = reqparse.RequestParser()
    parser.add_argument('registration', type=str, required=True, help='Registration of the car is required')
    parser.add_argument('vin', type=str, required=True, help='Vin of the car is required')
    parser.add_argument('make', type=str, required=True, help='Make of the car is required')
    parser.add_argument('model', type=str, required=True, help='Model of the car is required')
    parser.add_argument('first_registration_date', type=str, required=True,
                        help='First Registration Date of the car is required')
    parser.add_argument('production_year', type=str, required=True, help='Production year of the car is required')
    parser.add_argument('mileage', type=str, required=True, help='Mileage of the car is required')
    parser.add_argument('fuel_consumption', type=str, required=True, help='Fuel consumption of the car is required')
    parser.add_argument('fuel_type_id', type=int, required=True, help='Fuel type id of the car is required')
    parser.add_argument('vehicle_status_id', type=int, required=True, help='Vehicle status id of the car is required')

    def post(self) -> Response:
        """
        Post method to create a new car record.

        :return: The response containing the car ID if successful, or an error message with the appropriate HTTP status code.
        :rtype: Response
        """

        data = self.parser.parse_args()

        try:
            car_schema.validate(data)
            car = CarModel(**data)
            car.save()
            return car.as_dict(), 201, {'Content-Type': "application/json"}
        except IntegrityError as e:
            sa.session.rollback()
            return {"message": e.orig.args[1]}, 403
        except ValueError or TypeError as e:
            logging.info(e)
            return {"message": "Invalid request"}, 400
