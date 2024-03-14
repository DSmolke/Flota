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

load_insurances_data_blueprint = Blueprint('load_insurances_data', __name__, url_prefix='/load_insurances_data')


@load_insurances_data_blueprint.route('/csv', methods=['POST'])
def load_insurances_from_csv() -> Response:
    """
    Loads insurance data from a CSV file.

    Returns:
        Response: JSON response containing the loaded insurance data or an error message.
    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromCsvToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                   liability_model_constraints))
        loaded_insurances = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_insurances': [liability.as_dict() for liability in loaded_insurances]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_insurances_data_blueprint.route('/json', methods=['POST'])
def load_insurances_from_json() -> Response:
    """
    Load insurances from a JSON file.

    This method receives a POST request with a JSON file attached.
    It saves the file, processes its data, and returns the loaded insurances as a response.

    Returns:
        A Response object with the loaded insurances as a JSON payload and a status code.

    Raises:
        Exception: If any error occurs during the process.

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromJsonFileToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                        liability_model_constraints))
        loaded_insurances = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_insurances': [liability.as_dict() for liability in loaded_insurances]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_insurances_data_blueprint.route('/jsonl', methods=['POST'])
def load_insurances_from_jsonl() -> Response:
    """
    This method loads insurance data from a JSONL file and returns it as a response.

    Parameters:
        None

    Returns:
        Response: A Flask Response object with a JSON containing all loaded insurances or an error message.

    Example Usage:
        response = load_insurances_from_jsonl()
        print(response.json())

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromJsonlToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                              liability_model_constraints))
        loaded_insurances = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_insurances': [liability.as_dict() for liability in loaded_insurances]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_insurances_data_blueprint.route('/txt', methods=['POST'])
def load_insurances_from_txt() -> Response:
    """

    loads insurance data from a .txt file

    @return: Response object containing insurance data or error message
    @rtype: Response

    The method `load_insurances_from_txt` is responsible for processing insurance data from a .txt file. It is an endpoint that can be accessed via a POST request to the '/txt' route of
    * the load_insurances_data_blueprint.

    :param: None

    :raises: Exception - If there is any error during the processing of the insurance data.

    :return: Response object containing insurance data or error message.
    :rtype: Response

    Example usage:

    response = load_insurances_from_txt()
    print(response.json())
    # Output: {'all_insurances': [{'id': 1, 'name': 'John Doe', 'type': 'car'}, {'id': 2, 'name': 'Jane Smith', 'type': 'home'}]}

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromTxtToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                            liability_model_constraints))
        loaded_insurances = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_insurances': [liability.as_dict() for liability in loaded_insurances]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_insurances_data_blueprint.route('/xlsx', methods=['POST'])
def load_insurances_from_xlsx() -> Response:
    """
    Loads insurance data from an XLSX file and processes it.

    This method is a view function for handling a POST request to the '/xlsx' route of the 'load_insurances_data_blueprint'. It receives the data from the request, saves it to a file, processes
    * the data using a DataProcesor object and returns the processed data as a JSON response.

    Returns:
        Response: A JSON response containing the loaded insurance data.

    Raises:
        Exception: If an error occurs during the processing of the insurance data.

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromXlsxStrAdapterToLiabilitiesWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                       liability_model_constraints))
        loaded_insurances = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_insurances': [liability.as_dict() for liability in loaded_insurances]}, 200
    except Exception as e:
        return {'error': str(e)}, 404
