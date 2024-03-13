from pathlib import Path
from flask import Blueprint, request, Response

from app.processors import DataProcesor
from app.factories import (
    FromXlsxStrAdapterToCarsWithExpectedConstraintsDataFactory,
    FromTxtToCarsWithExpectedConstraintsDataFactory,
    FromJsonlToCarsWithExpectedConstraintsDataFactory,
    FromCsvToCarsWithExpectedConstraintsDataFactory,
    FromJsonFileToCarsWithExpectedConstraintsDataFactory
)
from app.routes.utils import save_file_from_request, delete_file_after_use
from app.validators.configuration import constraints

load_cars_data_blueprint = Blueprint('load_cars_data', __name__, url_prefix='/load_cars_data')


@load_cars_data_blueprint.route('/csv', methods=['POST'])
def load_cars_from_csv() -> Response:
    """Load cars data from a CSV file.

    This method is used to load cars data from a CSV file uploaded via a POST request. The CSV file is processed using a DataProcessor object with a specific data factory, and the resulting
    * loaded cars are returned as a JSON response.

    Parameters:
        None

    Returns:
        Response: A JSON response containing the loaded cars data or an error message.

    Example Usage:
        response = load_cars_from_csv()

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromCsvToCarsWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}', constraints))
        loaded_cars = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_cars': [c.as_dict() for c in loaded_cars]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_cars_data_blueprint.route('/json', methods=['POST'])
def load_cars_from_json() -> Response:
    """

    Load cars data from a JSON file

    This method is used to load cars data from a JSON file that is posted to the '/json' endpoint. It processes the data using a specified processor and returns the loaded cars in the form
    * of a response.

    Returns:
        A Response object containing the loaded cars data.

    Example usage:
        response = load_cars_from_json()

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromJsonFileToCarsWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}', constraints))
        loaded_cars = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_cars': [c.as_dict() for c in loaded_cars]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_cars_data_blueprint.route('/jsonl', methods=['POST'])
def load_cars_from_jsonl() -> Response:
    """

    This method `load_cars_from_jsonl` is an endpoint for handling a POST request to load car data from a JSONL file.

    Parameters:
        None

    Returns:
        Response: The response object with car data.

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromJsonlToCarsWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}', constraints))
        loaded_cars = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_cars': [c.as_dict() for c in loaded_cars]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_cars_data_blueprint.route('/txt', methods=['POST'])
def load_cars_from_txt() -> Response:
    """
    Load cars data from a .txt file and process it.

    This method is an endpoint for the '/txt' route with a POST request method. It receives a file from the request, saves it, processes the data using a DataProcessor, and returns the loaded
    * cars as a JSON response.

    Parameters:
        None

    Returns:
        Response: A JSON response containing all the loaded cars as a list of dictionaries, or an error message if an exception occurs.

    Example Usage:
        response = load_cars_from_txt()

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromTxtToCarsWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}', constraints))
        loaded_cars = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_cars': [c.as_dict() for c in loaded_cars]}, 200
    except Exception as e:
        return {'error': str(e)}, 404


@load_cars_data_blueprint.route('/xlsx', methods=['POST'])
def load_cars_from_xlsx() -> Response:
    """
    Loads car data from an XLSX file.

    This method is an HTTP route that accepts a POST request to load car data from an XLSX file. The method processes the file using a data processor and returns the loaded car data.

    Returns:
        Response: The HTTP response that includes the loaded car data or an error message.

    Raises:
        Exception: If an error occurs during the processing of the XLSX file.

    Example Usage:
        response = load_cars_from_xlsx()

    """
    try:
        filename = save_file_from_request(request)
        processor = DataProcesor(
            FromXlsxStrAdapterToCarsWithExpectedConstraintsDataFactory(f'{Path.cwd().absolute()}/{filename}',
                                                                       constraints))
        loaded_cars = processor.process()
        delete_file_after_use(filename=filename)
        return {'all_cars': [c.as_dict() for c in loaded_cars]}, 200
    except Exception as e:
        return {'error': str(e)}, 404
