from pathlib import Path

import pytest

from app.loaders.xlsx_loader import XlsxDataLoader


class TestValidCases:
    """
    Class: TestValidCases

    Description:
    This class contains test cases for the validity of loading data from a valid path.

    Methods:
    1. test_load_with_valid_path(test_data_path) -> None
       Description: This method tests the loading of data using a valid path.
       Parameters:
        - test_data_path: The path to the test data.
       Returns: None

    """
    def test_load_with_valid_path(self, test_data_path) -> None:
        """

        This method is used to test the functionality of loading data using a valid file path.

        Parameters:
        - self: The reference to the current instance of the class.
        - test_data_path: The relative path to the test data directory.

        Return Type: None

        Example Usage:
        test_load_with_valid_path(self, "data/test_files")

        """
        loader = XlsxDataLoader(f"{Path.cwd()}\\{test_data_path}\\cars.xlsx")

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
    Class: TestInvalidCases

    This class contains test cases for various invalid scenarios.

    Methods:
    1. test_load_with_invalid_path(test_data_path) -> None:
       This method tests the behavior when trying to load data with an invalid file path.

       Parameters:
       - test_data_path: The path to the test data directory.

       Raises:
       - FileNotFoundError: If the file specified by the given path is not found.

       Returns:
       - None

    """
    def test_load_with_invalid_path(self, test_data_path) -> None:
        """

        Test method to check the behavior of loading data with an invalid path.

        Parameters:
        - test_data_path (str): The relative path to the test data directory.

        Returns:
        None

        """
        loader = XlsxDataLoader(f"{Path.cwd()}\\{test_data_path}\\carss.xlsx")
        with pytest.raises(FileNotFoundError) as e:
            loader.load()
        assert e.type == FileNotFoundError
