import logging

from flask import Response, make_response, request
from flask_restful import Resource, reqparse, Api
from sqlalchemy.exc import IntegrityError
from app.validator.repair import repair_schema
from app.db.model import RepairModel
from app.db.configuration import sa

logging.basicConfig(level=logging.INFO)


class AddRepairResource(Resource):
    """
    Class representing a resource for adding repairs.

    Attributes:
        parser (RequestParser): Request parser for parsing and validating request data.

    Methods:
        post: Handles the POST request to add a new repair.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('car_id', type=int, required=True)
    parser.add_argument('repair_status', type=int, required=True)
    parser.add_argument('repair_description', type=str, required=True)
    parser.add_argument('approximate_duration', type=int, required=True)
    parser.add_argument('start_date', type=str, required=True)
    parser.add_argument('garage_name', type=str, required=True)
    parser.add_argument('garage_phone', type=str, required=True)

    def post(self) -> Response:
        """
        Handles the HTTP POST request to create a new repair.

        :param self: The current instance of the class.
        :return: A Response object with the result of the request.

        """
        request_data = self.parser.parse_args()

        try:
            repair_schema.validate(request_data)
            repair = RepairModel(**request_data)
            repair.save()
            return repair.as_dict(), 201, {'Content-Type': 'application/json'}

        except IntegrityError as e:
            sa.session.rollback()
            return {"message": e.orig.args[1]}, 403

        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class AllRepairsResource(Resource):
    """
    A class representing an API resource for retrieving all repairs.

    This class extends the `Resource` class from the `flask_restful` module.

    """
    def get(self) -> Response:
        """
        Get all repairs.

        :return: A response object containing all repairs in JSON format.
        :rtype: Response
        """
        repairs = RepairModel.get_all()
        response = make_response({'all_repairs': repairs})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        return response

class RepairsResource(Resource):
    """

    This class represents a resource endpoint for handling repairs.

    """
    def get(self, repair_id: int) -> Response:
        """
        :param repair_id: The ID of the repair to retrieve.
        :return: A Response object containing the repair as a dictionary if it exists, along with a status code of 200 (OK). If the repair does not exist, a dictionary with a "message" key and
        * a status code of 404 (Not Found) will be returned.
        """
        repair = RepairModel.get_by_id(repair_id)
        if repair:
            return repair.as_dict(), 200
        return {"message": "Repair does not exist"}, 404

    def delete(self, repair_id: int) -> Response:
        """
        Delete a repair with the given ID.

        :param repair_id: The ID of the repair to be deleted.
        :return: A dictionary containing a message indicating the status of the deletion and a status code.
                 If the repair is deleted successfully, the message will be "Repair has been deleted" and
                 the status code will be 200. If the repair is not found, the message will be "Repair not found"
                 and the status code will be 404.
        """
        repair_to_delete = RepairModel.get_by_id(repair_id)
        if repair_to_delete:
            repair_to_delete.delete()
            return {"message": "Repair has been deleted"}, 200
        return {"message": "Repair not found"}, 404

    def patch(self, repair_id: int) -> Response:
        """
        Update an existing repair with the provided repair_id.

        :param repair_id: The ID of the repair to update.
        :type repair_id: int
        :return: A response containing either the updated repair or an error message.
        :rtype: Response
        """
        try:
            data = request.get_json()
            repair_schema.validate(data)
            repair = RepairModel.get_by_id(repair_id)
            if repair:
                repair.update(data)
                return repair.as_dict(), 200
            return {"message": "Repair does not exist"}, 404
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class RepairEndPointsMapper:
    """
    Class responsible for mapping repair endpoints to their respective routes.

    :param api: An instance of Api class.
    """
    endpoints_with_routes = [
        (AddRepairResource, '/repairs'),
        (AllRepairsResource, '/repairs/all'),
        (RepairsResource, '/repairs/<int:repair_id>'),
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
