from flask import request, Response, make_response
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError


from app.db.configuration import sa
from app.db.model import MotModel
from app.validator.mot import mot_schema


class AllMotsResource(Resource):
    """
    Resource class for retrieving all mots.

    :return: JSON response containing all mots.
    :rtype: flask.Response
    """
    def get(self) -> Response:
        """
        Get all mots from the MotModel.

        :return: Response object containing all mots in JSON format.
        """
        mots = MotModel.get_all()
        response = make_response({'all_mots': mots})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        return response


class MotsResource(Resource):
    def get(self, mot_id: int) -> Response:
        """

        :param mot_id: The ID of the MOT to be retrieved.
        :type mot_id: int
        :return: A dictionary representing the MOT if it exists, otherwise a dictionary with an error message.
        :rtype: Response
        :raises: None

        """
        mot = MotModel.get_by_id(mot_id)
        if mot:
            return mot.as_dict(), 200
        return {"message": "Mot does not exist"}, 404

    def delete(self, mot_id: int) -> Response:
        """
        Deletes a Mot with the given ID.

        :param mot_id: The ID of the Mot to delete.
        :return: A Response object containing a message and status code.
        """
        mot_to_delete = MotModel.get_by_id(mot_id)
        if mot_to_delete:
            mot_to_delete.delete()
            return {"message": "Mot has been deleted"}, 200
        return {"message": "Mot not found"}, 404

    def patch(self, mot_id: int) -> Response:
        """
        Update the Mot with the given ID.

        :param mot_id: The ID of the Mot to update.
        :type mot_id: int
        :return: The updated Mot as a dictionary.
        :rtype: Response
        """
        try:
            data = request.get_json()
            mot_schema.validate(data)
            mot = MotModel.get_by_id(mot_id)
            if mot:
                mot.update(data)
                return mot.as_dict(), 200
            return {"message": "Mot does not exist"}, 404
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400


class MotResourceAdd(Resource):
    """
    MotResourceAdd class is a subclass of Resource class. It handles the POST request to add a new MOT (Ministry of Transport) record.

    Attributes:
        parser (RequestParser): A RequestParser object for parsing the request arguments.

    Methods:
        post(self) -> Response:
            Handles the POST request and adds a new MOT record.

            Returns:
                - If the MOT record is added successfully, returns the MOT ID, status code 201, and content type header.
                - If there is an integrity error, rolls back the session and returns the error message and status code 403.
                - If there is a value or type error in the request, returns the error message and status code 400.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('legal_identifier', type=str, required=True, help='Legal identifier of mot is required')
    parser.add_argument('start_date', type=str, required=True, help='Start date of mot is required')
    parser.add_argument('end_date', type=str, required=True, help='End date of mot is required')
    parser.add_argument('car_registration_number', type=str, required=True, help='Car registration number of mot is required')
    parser.add_argument('img_url', type=str, required=True,
                        help='Image url of the mot is required')
    parser.add_argument('active', type=bool, required=True, help='Active flag of mot is required')

    def post(self) -> Response:
        """
        Endpoint to handle POST requests.

        :return: If the request is valid and the data passes validation, it will save the data
                 to the database and return the ID of the saved record along with a status
                 code 201 and Content-Type header set to "application/json". If the request
                 fails due to an integrity error, it will roll back the session and return
                 a JSON object with an error message and a status code 403. If the request
                 fails due to a value or type error, it will return a JSON object with an
                 "Invalid request" message and a status code 400.
        """
        data = self.parser.parse_args()

        try:
            mot_schema.validate(data)
            mot = MotModel(**data)
            mot.save()
            return mot.id, 201, {'Content-Type': "application/json"}
        except IntegrityError as e:
            sa.session.rollback()
            return {"message": e.orig.args[1]}, 403
        except ValueError or TypeError:
            return {"message": "Invalid request"}, 400
