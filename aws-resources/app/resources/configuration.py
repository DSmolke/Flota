from pathlib import Path
import boto3
from app.env_variables import (
    AWS_ACCESS_KEY,
    AWS_SECRET_ACCESS_KEY,
    BUCKET_NAME,
    BUCKET_SUBFOLDER_NAME
)

class FileUploadConfig:
    """
    Class to handle file upload and sending to AWS S3.

    Parameters:
        request: Flask request object.

    Attributes:
        aws_access_key_id (str): AWS access key ID.
        aws_secret_access_key (str): AWS secret access key.
        bucket_name (str): Name of the S3 bucket.
        bucket_subfolder_name (str): Name of the subfolder within the S3 bucket.
        s3 (boto3.client): Boto3 S3 client object.
        file (FileStorage): File object.
        filename (str): Name of the file.

    Methods:
        send_to_aws(): Saves the file locally, uploads it to S3, and returns the URL of the uploaded file.

    Raises:
        ValueError: If no file is provided.

    """
    def __init__(self, request):
        self.aws_access_key_id = AWS_ACCESS_KEY
        self.aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        self.bucket_name = BUCKET_NAME
        self.bucket_subfolder_name = BUCKET_SUBFOLDER_NAME

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

        self.file = request.files.get('file')
        self.filename = self.file.filename

    def send_to_aws(self):
        """
        Uploads the file to AWS S3 bucket.

        :return: Dictionary containing the URL of the uploaded file
        :rtype: dict
        :raises ValueError: If no file is provided
        """
        if self.file:
            self.file.save(self.filename)

            s3_response = self.s3.upload_file(
                self.filename,
                self.bucket_name,
                f'{self.bucket_subfolder_name}/{self.filename}'
            )

            Path.cwd().joinpath(self.filename).unlink()

            url = f'https://{self.bucket_name}.s3.eu-central-1.amazonaws.com/{self.bucket_subfolder_name}/{self.filename}'
            return {
                'url': url
            }
        raise ValueError('No file provided')


class FileDeleteConfig:
    """
    Delete the file from AWS S3 bucket.

    :returns: A dictionary containing the URL of the deleted file in the S3 bucket.
    :rtype: dict

    :raises ValueError: If no file is provided in the request.
    """
    def __init__(self, request):
        self.aws_access_key_id = AWS_ACCESS_KEY
        self.aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        self.bucket_name = BUCKET_NAME
        self.bucket_subfolder_name = BUCKET_SUBFOLDER_NAME

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

        self.file = request.json.get('file', None).split('/')[-1]

    def delete_from_aws(self):
        """
        Deletes a file from AWS S3 bucket.

        :return: A dictionary containing the URL of the deleted object.
        :raises ValueError: If no file is provided.
        """
        if self.file:
            s3_response = self.s3.delete_object(
                Bucket=self.bucket_name,
                Key=f"{self.bucket_subfolder_name}/{self.file}",
            )

            return {
                'url': s3_response
            }
        raise ValueError('No file provided')
