from pathlib import Path

import pytest

from app.loaders.txt_loader import TxtDataLoader

class TestValidCases:
    """A class that contains test cases for validating the behavior of the `load_with_valid_path` method.

        This class defines a set of test cases to verify the behavior of the `load_with_valid_path` method of the `TxtDataLoader` class.
        The purpose of these test cases is to ensure that the method correctly loads data from a valid file path and returns the expected result.

        Attributes:
            None

        Methods:
            test_load_with_valid_path(test_data_path) -> None: A test case that verifies the behavior of the `load_with_valid_path` method.

    """
    def test_load_with_valid_path(self, test_data_path) -> None:
        """

            Test method to verify the loading of data from a valid path.

            Args:
                self: The instance of the test class.
                test_data_path: The relative path to the test data directory.

            Returns:
                None

            Raises:
                AssertionError: If the loaded data does not match the expected result.

            Example usage:
                test_load_with_valid_path(self, "data")
        """
        loader = TxtDataLoader(f"{Path.cwd()}\\{test_data_path}\\cars.csv")

        assert loader.load() == [{
            "id": '1',
            "registration_number": "DPL96RR",
            "first_registration_date": "2012-03-15",
            "vin": "4Y1SL65848Z411439",
            "brand": "BMW",
            "model": "SERIES 3"
        }]

class TestInvalidCases:
    def test_load_with_invalid_path(self, test_data_path) -> None:
        """
        Test method to check if an exception is raised for an invalid file path.

        Args:
            test_data_path: A string representing the test data path.

        Returns:
            None

        Raises:
            FileNotFoundError: If the file path is not found.

        """
        loader = TxtDataLoader(f"{Path.cwd()}\\{test_data_path}\\carss.csv")
        with pytest.raises(FileNotFoundError) as e:
            loader.load()
        assert e.type == FileNotFoundError
