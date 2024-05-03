from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
import logging
logging.basicConfig(level=logging.ERROR)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response:
        response.data['status_code'] = response.status_code
        response.data['author'] = 'DSmolke'
    return response
