from pathlib import Path

import pytest

from app.loaders.jsonl_loader import JsonlDataLoader


class TestValidCases:
    """

    The `TestValidCases` class is used to test the functionality of loading data from a valid path using the `JsonlDataLoader` class.

    Attributes:
    - None

    Methods:
    - `test_load_with_valid_path(test_data_path) -> None`:
        This method tests the `load` method of the `JsonlDataLoader` class by loading data from a valid path. It takes the `test_data_path`
        as a parameter, which specifies the path to the test data directory.

        Parameters:
        - `test_data_path` (str): The path to the test data directory.

        Returns:
        - None

        Raises:
        - None

    Example Usage:
        ```
        test_case = TestValidCases()
        test_case.test_load_with_valid_path("test_data")
        ```
    """
    def test_load_with_valid_path(self, test_data_path) -> None:
        """
        This method tests the functionality of loading data from a valid path using the JsonlDataLoader.

        Parameters:
        - self: The instance of the test class.
        - test_data_path: The relative path to the test data folder.

        Returns:
        None

        Raises:
        No exceptions are raised by this method.

        Example usage:
        test_load_with_valid_path(self, "test_data")"""
        loader = JsonlDataLoader(f"{Path.cwd()}\\{test_data_path}\\cars.jsonl")
        loaded_dict = {
            "id": 1,
            "registration_number": "DPL96RR",
            "first_registration_date": "2012-03-15",
            "vin": "4Y1SL65848Z411439",
            "brand": "BMW",
            "model": "SERIES 3"
        }
        assert loader.load() == [loaded_dict, loaded_dict]

class TestInvalidCases:
    """
    Check if FileNotFoundError is raised when loading data with an invalid path.

    Raises:
        FileNotFoundError: If the data file is not found.

    Returns:
        None
    """
    def test_load_with_invalid_path(self) -> None:
        """

        Method Name: test_load_with_invalid_path

        Parameters: self (implicit), None

        Return Type: None

        Description:
        This method tests the behavior of the `load` method in the `JsonlDataLoader` class when an invalid file path is provided. It verifies that a `FileNotFoundError` is raised.

        Example Usage:
        test_load_with_invalid_path()

        """
        loader = JsonlDataLoader(f"{Path.cwd()}\\data\\carss.jsonl")
        with pytest.raises(FileNotFoundError) as e:
            loader.load()
        assert e.type == FileNotFoundError
