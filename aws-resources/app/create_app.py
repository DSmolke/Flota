import logging

from flask import Flask, request
from flask_cors import CORS

from app.resources.configuration import FileUploadConfig, FileDeleteConfig

# ----------------------------------------------------------------------
# LOGGER CONFIGURATION
# ----------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


def main() -> Flask:
    with app.app_context():
        # ----------------------------------------------------------------------
        # CORS CONFIGURATION
        # ----------------------------------------------------------------------
        CORS(app, resources={
            '/*': {
                'allow_headers': [
                    'accept',
                    'accept-encoding',
                    'authorization',
                    'content-type'
                ],
                'methods': [
                    'delete',
                    'get',
                    'post',
                    'patch',
                    'put',
                    'options'
                ],
                'origins': [
                    'http://localhost:8000',
                    'http://localhost:3000',
                ]
            }
        })

        # ----------------------------------------------------------------------
        # AWS CONFIGURATION
        # ----------------------------------------------------------------------
        @app.route("/file", methods=['POST'])
        def upload_file():
            """
            API endpoint for uploading a file.

            :return: Returns the response from the send_to_aws() method as well as the HTTP status code 201 (Created) if successful.
                     Returns the message 'No file provided' and the HTTP status code 400 (Bad Request) if no file is provided.
            """
            try:
                file_upload_config = FileUploadConfig(request)
                return file_upload_config.send_to_aws(), 201
            except ValueError as e:
                return {'message': 'No file provided'}, 400

        @app.route('/file', methods=['DELETE'])
        def delete_file():
            """
            Delete a file from AWS

            :return: The result of the file deletion request
            """
            file_delete_config = FileDeleteConfig(request)
            return file_delete_config.delete_from_aws(), 201

        return app
