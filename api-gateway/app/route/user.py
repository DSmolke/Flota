import logging

from flask import request, Response
from flask_restful import Resource, reqparse
from datetime import datetime
from app.db.model import UserModel
from app.email.configuration import MailSender

logging.basicConfig(level=logging.DEBUG)

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username cannot be empty')
    parser.add_argument('password', type=str, required=True, help='Password cannot be empty')
    parser.add_argument('email', type=str, required=True, help='Email cannot be empty')

    def post(self) -> Response:
        try:
            request_data = UserResource.parser.parse_args()

            if UserModel.find_by_username(request_data['username']):
                return {'message': 'User already exists'}, 400

            if UserModel.find_by_email(request_data['email']):
                return {'message': 'Email already exists'}, 400

            user = UserModel(**request_data)
            user.save_or_update()

            MailSender.send_activation_email(user.id, user.username, user.email)

            return {'message': 'User created'}, 201
        except Exception as e:
            logging.debug(e.args)
            return {'message': "Service that application relies on didn't respond"}, 503


class UserActivationResource(Resource):

    def get(self) -> Response:
        try:
            # Checks if activation timestamp is not expired
            timestamp = float(request.args.get('timestamp'))
            timestamp_now = datetime.utcnow().timestamp() * 1000
            user_id = request.args.get('id')
            user_to_activate = UserModel.find_by_id(user_id)

            if user_to_activate.is_activated():
                return {'message': 'User already activated'}, 400

            if timestamp < timestamp_now:

                if user_to_activate:
                    MailSender.send_activation_email(user_to_activate.id, user_to_activate.username, user_to_activate.email)
                    return {'message': 'Activation link is expired. New one was sent to your email'}, 201
                return Response({'message': 'User activation error'}, 400)

            user_id = request.args.get('id')
            user_to_activate = UserModel.find_by_id(user_id)
            if user_to_activate:
                user_to_activate.active = True
                user_to_activate.save_or_update()
                return user_to_activate.as_dict(), 200
            return {'message': 'User activation error'}, 400

        except Exception as e:
            logging.info(e.args[0])
            return Response({'message': f'Something went wrong'}, 400)
