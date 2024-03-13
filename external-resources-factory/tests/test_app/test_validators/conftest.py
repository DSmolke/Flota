import pytest
from easyvalid_data_validator.constraints import Constraint

from app.validators.json_dict_validator import JsonDictValidator


@pytest.fixture(scope="session")
def mot_validator():
    """
    Mot Validator

    This method returns a `JsonDictValidator` object that is used to validate a MOT (Ministry of Transport) object.

    Parameters:
        None

    Returns:
        `JsonDictValidator`: A validator object that can be used to validate MOT objects.

    Example:
        mot_validator = mot_validator()

        # Create a MOT object
        mot = {
            "mot_id": 1,
            "start_date": "2022-01-01 09:00:00.000",
            "end_date": "2022-01-02 18:00:00.000",
            "car_id": 1234
        }

        # Validate the MOT object
        is_valid = mot_validator.validate(mot)

        if is_valid:
            print("MOT is valid")
        else:
            print("MOT is invalid")
    """
    return JsonDictValidator({
        "mot_id": {Constraint.INT_GRATER: 0},
        "start_date": {Constraint.STRING_REGEX: r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}"},
        "end_date": {Constraint.STRING_REGEX: r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}"},
        "car_id": {Constraint.INT_GRATER: 0}
    }
    )

@pytest.fixture(scope="session")
def two_elements_valid_mot_data():
    """

    This method returns a list of two dictionaries, each representing a valid MOT (Ministry of Transport) data.

    The dictionaries have the following keys:
    - mot_id: An integer representing the MOT ID.
    - start_date: A string representing the start date of the MOT in the format "YYYY-MM-DD HH:MM:SS.SSS".
    - end_date: A string representing the end date of the MOT in the format "YYYY-MM-DD HH:MM:SS.SSS".
    - car_id: An integer representing the car ID.

    Example usage:
        mot_data = two_elements_valid_mot_data()

    Output:
        [
            {
                "mot_id": 1,
                "start_date": "2022-03-15 00:00:00.000",
                "end_date": "2023-03-15 00:00:00.000",
                "car_id": 1
            },
            {
                "mot_id": 2,
                "start_date": "2023-03-15 00:00:00.000",
                "end_date": "2024-03-15 00:00:00.000",
                "car_id": 2
            },
        ]

    """
    data = [
        {
            "mot_id": 1,
            "start_date": "2022-03-15 00:00:00.000",
            "end_date": "2023-03-15 00:00:00.000",
            "car_id": 1
        },
        {
            "mot_id": 2,
            "start_date": "2023-03-15 00:00:00.000",
            "end_date": "2024-03-15 00:00:00.000",
            "car_id": 2
        },
    ]
    return data
