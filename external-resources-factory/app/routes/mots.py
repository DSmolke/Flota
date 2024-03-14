from pathlib import Path
from flask import Blueprint, request, Response

from app.factories import (
    FromXlsxStrAdapterToLiabilitiesWithExpectedConstraintsDataFactory,
    FromTxtToLiabilitiesWithExpectedConstraintsDataFactory,
    FromJsonlToLiabilitiesWithExpectedConstraintsDataFactory,
    FromJsonFileToLiabilitiesWithExpectedConstraintsDataFactory,
    FromCsvToLiabilitiesWithExpectedConstraintsDataFactory

)
from app.processors import DataProcesor
from app.routes.utils import save_file_from_request, delete_file_after_use
from app.validators.configuration import liability_model_constraints

load_mots_data_blueprint = Blueprint('load_mots_data', __name__, url_prefix='/load_mots_data')


@load_mots_data_blueprint.route('/csv', methods=['POST'])
def load_mots_from_csv() -> Response:
    """

    This method, `load_mots_from_csv()`, is a route handler for the `/csv` endpoint in the `load_mots_data_blueprint` blueprint. It is used to load MOTs (liabilities) from a CSV file and
    * process them using a data processor.

    Parameters:
        None

    Returns:
        - If successful, returns a `Response` object with a JSON payload containing all loaded MOTs as a list of dictionaries. The status code is set to 200.
        - If an error occurs, returns a `Response` object with a JSON payload containing an error message. The status code is set to 404.

    Example Usage:
    ```
    response = load_mots_from_csv()
    if response.status_code == 200:
        all_mots = response.json()["all_mots"]
        for mot in all_mots:
            print(mot)
    else:
        error_message = response.json()["error"]
        print(f"Error: {error_message}")
    ```
    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromCsvToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                   liability_model_constraints))
        loaded_mots = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_mots': [liability.as_dict() for liability in loaded_mots]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_mots_data_blueprint.route('/json', methods=['POST'])
def load_mots_from_json() -> Response:
    """
    Loads MOTS (Measurements, Observations, and Test Results) data from a JSON file.

    This method is an endpoint for the '/json' route and accepts a POST request. It processes the uploaded JSON file containing MOTS data and returns a response.

    Returns:
        A `Response` object containing the processed MOTS data or an error message.

    Example:
        ```
        response = load_mots_from_json()
        ```
    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromJsonFileToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                        liability_model_constraints))
        loaded_mots = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_mots': [liability.as_dict() for liability in loaded_mots]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_mots_data_blueprint.route('/jsonl', methods=['POST'])
def load_mots_from_jsonl() -> Response:
    """
    Loads MOTs (Ministry of Transportations) data from a JSONL file and processes it.

    :return: Response object containing the processed MOTs data.
    :rtype: Response
    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromJsonlToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                              liability_model_constraints))
        loaded_mots = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_mots': [liability.as_dict() for liability in loaded_mots]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_mots_data_blueprint.route('/txt', methods=['POST'])
def load_mots_from_txt() -> Response:
    """

    [POST] /txt

    Loads MOTS (Methods of Technical Specification) data from a TXT file.

    Returns:
        - Response: The response object containing the loaded MOTS data.

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromTxtToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                            liability_model_constraints))
        loaded_mots = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_mots': [liability.as_dict() for liability in loaded_mots]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_mots_data_blueprint.route('/xlsx', methods=['POST'])
def load_mots_from_xlsx() -> Response:
    """
    load_mots_from_xlsx() method is a POST request endpoint that processes data from an uploaded Excel file and returns the loaded MOTs (Modified Organism Traits) as a JSON response.

    Parameters:
        None

    Returns:
        Response: An HTTP response object containing the loaded MOTs as JSON data.

    HTTP Method:
        POST

    URL Route:
        /xlsx

    Example Usage:
        Suppose you have a Flask application with the defined route '/xlsx'. You can send a POST request to this endpoint to upload an Excel file and receive the loaded MOTs in JSON format
    *.

        Example Request:
            POST /xlsx
            Content-Type: multipart/form-data
            Body: <Excel file upload>

        Example Response:
            Status code: 200
            Content-Type: application/json
            Body: {
                "all_mots": [
                    {"mots_property1": "value1", "mots_property2": "value2", ...},
                    {"mots_property1": "value3", "mots_property2": "value4", ...},
                    ...
                ]
            }

    Exceptions:
        If an exception occurs during the processing of the Excel file, a 404 error response with an error message will be returned.

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromXlsxStrAdapterToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                       liability_model_constraints))
        loaded_mots = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_mots': [liability.as_dict() for liability in loaded_mots]}, 200
    except Exception as e:
        return {'error': str(e)}, 404
