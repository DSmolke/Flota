
from pathlib import Path

import pytest

from app.loaders.json_loader import JsonDataLoader


class TestValidCases:
    """
    Class: TestValidCases

    Description:
    A class for testing valid cases of loading data using a JsonDataLoader.

    Methods:
    - test_load_with_valid_path(test_data_path) -> None
        - Description: Tests loading data using a valid file path.
        - Parameters:
            - test_data_path: str - The path of the directory containing the test data.
        - Returns: None
    """
    def test_load_with_valid_path(self, test_data_path) -> None:
        """
        Loads and asserts that the JSON data loaded from a valid file path is equal to a predefined list of dictionaries representing car data.

        Parameters:
        - self: the current object instance.
        - test_data_path: a string representing the path to the directory containing the test data file.

        Return:
        - None

        Example:

        test_load_with_valid_path(self, test_data_path)
        """
        loader = JsonDataLoader(f"{Path.cwd()}\\{test_data_path}\\cars.json")
        assert loader.load() == [{
            "id": 1,
            "registration_number": "DPL96RR",
            "first_registration_date": "2012-03-15",
            "vin": "4Y1SL65848Z411439",
            "brand": "BMW",
            "model": "SERIES 3"
        }]

class TestInvalidCases:
    """
    Class for testing invalid cases in JsonDataLoader.

    Methods:
    - test_load_with_invalid_path: Test loading with an invalid file path.
    """
    def test_load_with_invalid_path(self) -> None:
        """
        Test method to verify the behavior of the JsonDataLoader when loading data with an invalid path.

        :param self: The instance of the test case.
        :type self: TestCase

        :returns: None
        :rtype: None
        """
        loader = JsonDataLoader(f"{Path.cwd()}\\data\\carss.json")
        with pytest.raises(FileNotFoundError) as e:
            loader.load()
        assert e.type == FileNotFoundError
