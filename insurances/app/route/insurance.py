from flask import request, Response, make_response
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError


from app.db.configuration import sa
from app.db.model import InsuranceModel
from app.validator.insurance import insurance_schema


class AllInsurancesResource(Resource):
    """Class AllInsurancesResource

    This class is a resource that handles the GET request for retrieving all insurances.

    Methods:
        - get: Retrieves all insurances.

    """
    def get(self) -> Response:
        """
        Retrieve all insurances.

        :return: A response containing a JSON object with all insurance records.
        :rtype: Response
        """
        insurances = InsuranceModel.get_all()
        response = make_response({'all_insurances': insurances})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        return response


class InsurancesResource(Resource):
    """

    InsurancesResource(Resource)
    --------------------------

    This class represents a resource for managing insurance objects.

    Methods
    -------
    get(self, insurance_id: int) -> Response:
        This method handles the GET request for retrieving an insurance object by its ID.

        Parameters:
        - insurance_id (int): The ID of the insurance object to retrieve.

        Returns:
        - Response: The response containing the insurance object as a dictionary and the status code 200 if the insurance exists, or a response with the message "Insurance does not exist
    *" and the status code 404 if the insurance does not exist.

    delete(self, insurance_id: int) -> Response:
        This method handles the DELETE request for deleting an insurance object by its ID.

        Parameters:
        - insurance_id (int): The ID of the insurance object to delete.

        Returns:
        - Response: The response with the message "Insurance has been deleted" and the status code 200 if the insurance is successfully deleted, or a response with the message "Insurance
    * not found" and the status code 404 if the insurance is not found.

    patch(self, insurance_id: int) -> Response:
        This method handles the PATCH request for updating an insurance object by its ID.

        Parameters:
        - insurance_id (int): The ID of the insurance object to update.

        Returns:
        - Response: The response containing the updated insurance object as a dictionary and the status code 200 if the insurance exists and the request is valid, or a response with the
    * message "Insurance does not exist" and the status code 404 if the insurance does not exist, or a response with the message "Invalid request" and the status code 400 if the request
    * is invalid.


    """
    def get(self, insurance_id: int) -> Response:
        """
        :param insurance_id: The ID of the insurance to retrieve.
        :return: A Response object containing the insurance information if found, or a JSON object with an error message if the insurance does not exist.
        """
        insurance = InsuranceModel.get_by_id(insurance_id)
        if insurance:
            return insurance.as_dict(), 200
        return {"message": "Insurance does not exist"}, 404

    def delete(self, insurance_id: int) -> Response:
        """
        Delete insurance by ID.

        :param insurance_id: ID of the insurance to be deleted.
        :type insurance_id: int
        :return: Response with a message indicating the status of the delete operation.
        :rtype: Response
        """
        insurance_to_delete = InsuranceModel.get_by_id(insurance_id)
        if insurance_to_delete:
            insurance_to_delete.delete()
            return {"message": "Insurance has been deleted"}, 200
        return {"message": "Insurance not found"}, 404

    def patch(self, insurance_id: int) -> Response:
        """
        :param insurance_id: The ID of the insurance to be patched.
        :return: The patched insurance as a dictionary, with HTTP status code 200 if successful.
                 If the insurance does not exist, returns a dictionary with a "message" key and HTTP status code 404.
                 If the request is invalid, returns a dictionary with a "message" key and HTTP status code 400.
        """
        try:
            data = request.get_json()
            insurance_schema.validate(data)
            insurance = InsuranceModel.get_by_id(insurance_id)
            if insurance:
                insurance.update(data)
                return insurance.as_dict(), 200
            return {"message": "Insurance does not exist"}, 404
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class InsuranceResourceAdd(Resource):
    """
    Resource class to handle adding insurance data.

    :ivar parser: RequestParser object to parse and validate request arguments.
    :vartype parser: RequestParser

    """
    parser = reqparse.RequestParser()
    parser.add_argument('legal_identifier', type=str, required=True, help='Legal identifier of insurance is required')
    parser.add_argument('start_date', type=str, required=True, help='Start date of insurance is required')
    parser.add_argument('end_date', type=str, required=True, help='End date of insurance is required')
    parser.add_argument('car_registration_number', type=str, required=True, help='Car registration number of insurance is required')
    parser.add_argument('img_url', type=str, required=True,
                        help='Image url of the insurance is required')
    parser.add_argument('active', type=bool, required=True, help='Active flag of insurance is required')

    def post(self) -> Response:
        """
        Process a POST request to create a new insurance entry.

        :return:
            - If the request is valid and the insurance entry is successfully created:
                - The ID of the created insurance entry.
                - Status code 201 indicating successful creation.
                - Content-Type header set to application/json.
            - If the request fails due to integrity error (duplicate entry):
                - A JSON object with a message describing the error.
                - Status code 403 indicating forbidden access.
            - If the request fails due to invalid data or incorrect data types:
                - A JSON object with a message indicating an invalid request.
                - Status code 400 indicating bad request.
        """
        data = self.parser.parse_args()

        try:
            insurance_schema.validate(data)
            insurance = InsuranceModel(**data)
            insurance.save()
            return insurance.as_dict(), 201, {'Content-Type': "application/json"}
        except IntegrityError as e:
            sa.session.rollback()
            return {"message": e.orig.args[1]}, 403
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400
