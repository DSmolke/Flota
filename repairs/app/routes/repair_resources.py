import logging

from flask import Response, make_response, request
from flask_restful import Resource, reqparse, Api
from sqlalchemy.exc import IntegrityError
from app.validator.repair import repair_schema
from app.db.model import RepairModel

logging.basicConfig(level=logging.INFO)


class AddRepairResource(Resource):


    def post(self) -> Response:
        pass

class AllRepairsResource(Resource):

    def get(self) -> Response:
       pass

class RepairsResource(Resource):

    def get(self, repair_id: int) -> Response:
        pass

    def delete(self, repair_id: int) -> Response:
       pass

    def patch(self, repair_id: int) -> Response:
       pass


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
