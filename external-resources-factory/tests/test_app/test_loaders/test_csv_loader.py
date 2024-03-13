from pathlib import Path

import pytest

from app.loaders.csv_loader import CsvDataLoader


class TestValidCases:
    """
    The TestValidCases class is used to test the 'load()' method of the 'CsvDataLoader' class with a valid path.

    Attributes:
        - None

    Methods:
        - test_load_with_valid_path(test_data_path)

    test_load_with_valid_path(test_data_path) -> None:
        This method tests the 'load()' method of the 'CsvDataLoader' class with a valid path.

        Args:
            - self (object): The CsvDataLoader object.
            - test_data_path (str): The path to the test data directory.

        Returns:
            - None

        Raises:
            - AssertionError: If the loaded data does not match the expected result.
    """
    def test_load_with_valid_path(self, test_data_path) -> None:
        """
        Test the 'load()' method of the 'CsvDataLoader' class with a valid path.

        Args:
            self (object): The CsvDataLoader object.
            test_data_path (str): The path to the test data directory.

        Returns:
            None

        Raises:
            AssertionError: If the loaded data does not match the expected result.
        """
        loader = CsvDataLoader(f"{Path.cwd()}\\{test_data_path}\\cars.csv")
        assert loader.load() == [{
            "id": '1',
            "registration_number": "DPL96RR",
            "first_registration_date": "2012-03-15",
            "vin": "4Y1SL65848Z411439",
            "brand": "BMW",
            "model": "SERIES 3"
        }]

class TestInvalidCases:
    """

    This class represents a set of test cases for the CsvDataLoader class when provided with invalid cases.

    """
    def test_load_with_invalid_path(self) -> None:
        """

        """
        loader = CsvDataLoader(f"{Path.cwd()}\\data\\carss.csv")
        with pytest.raises(FileNotFoundError) as e:
            loader.load()
        assert e.type == FileNotFoundError
