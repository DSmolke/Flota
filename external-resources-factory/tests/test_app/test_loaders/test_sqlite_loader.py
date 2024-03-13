import pytest
from pathlib import Path
from sqlite3 import OperationalError

from app.loaders.sqlite_loader import Sqlite3DataLoader


class TestValidCases:
    """
    Class representing test cases for loading data with valid path, query, and keys.

    Methods:
    - test_load_with_valid_path_query_keys(mots_basic_query, test_data_path): Executes the test for loading data with a valid path, query, and keys.

    Attributes:
    - mots_basic_query: The basic query to be executed.
    - test_data_path: The path to the test data.
    """
    def test_load_with_valid_path_query_keys(self, mots_basic_query, test_data_path) -> None:
        """
        This method is used to test the `load` method of the `Sqlite3DataLoader` class when provided with a valid path, query, and keys.

        Parameters:
                self (object): The instance of the test class.
                mots_basic_query (str): The query string to be used for loading data.
                test_data_path (str): The path to the test data directory.

        Returns:
                None: This method does not return anything.

        """
        # when tests are started from /tests
        valid_path = f"{Path.cwd()}\\{test_data_path}\\test_db1.db"
        valid_query = mots_basic_query
        valid_keys = ["id", "start_date", "end_date", "car_id"]
        loader = Sqlite3DataLoader(valid_path, valid_query, valid_keys)

        assert loader.load() == [
            {
                "id": 1,
                "start_date": "2022-03-15",
                "end_date": "2023-03-15",
                "car_id": 1
            }]

class TestInvalidCases:
    """
    Class: TestInvalidCases

    A class that contains test cases for testing invalid scenarios.

    Methods:
    - test_load_with_invalid_path(mots_basic_query, test_data_path) -> None:
      This method tests loading data with an invalid file path.
      Parameters:
        - mots_basic_query: The basic query for the MOTS table.
        - test_data_path: The path to the test data.
      Returns: None

    - test_load_with_invalid_keys(mots_basic_query, test_data_path) -> None:
      This method tests loading data with invalid keys.
      Parameters:
        - mots_basic_query: The basic query for the MOTS table.
        - test_data_path: The path to the test data.
      Returns: None

    - test_loader_with_invalid_query(people_basic_query, test_data_path) -> None:
      This method tests loading data with an invalid query.
      Parameters:
        - people_basic_query: The basic query for the People table.
        - test_data_path: The path to the test data.
      Returns: None
    """
    def test_load_with_invalid_path(self, mots_basic_query, test_data_path) -> None:
        """
        Test the load method of Sqlite3DataLoader with an invalid path.

        Args:
            mots_basic_query (str): The MOTS basic query.
            test_data_path (str): The path to the test data directory.

        Returns:
            None

        Raises:
            AssertionError: If the exception type raised is not OperationalError.
        """
        invalid_path = f"{Path.cwd()}\\{test_data_path}\\fake_db.db"
        valid_query = mots_basic_query
        valid_keys = ["id", "start_date", "end_date", "car_id"]
        loader = Sqlite3DataLoader(invalid_path, valid_query, valid_keys)

        with pytest.raises(OperationalError) as e:
            loader.load()
        assert e.type == OperationalError

    def test_load_with_invalid_keys(self, mots_basic_query, test_data_path) -> None:
        """
        Test method for loading data with invalid keys.

        Parameters:
        - mots_basic_query (str): The basic query used for loading data.
        - test_data_path (str): The path to the test data.

        Returns:
        - None

        Example:
            mots_basic_query = "SELECT * FROM table"
            test_data_path = "data"
            test_load_with_invalid_keys(mots_basic_query, test_data_path)
        """
        valid_path = f"{Path.cwd()}\\{test_data_path}\\test_db1.db"
        valid_query = mots_basic_query
        valid_keys = ["start_date", "end_date", "car_id"]
        loader = Sqlite3DataLoader(valid_path, valid_query, valid_keys)

        # loader has nothing to do with validation, so it shouldn't validate structure of loaded data
        assert loader.load() != [
            {
                "id": 1,
                "start_date": "2022-03-15",
                "end_date": "2023-03-15",
                "car_id": 1
            }]

    def test_loader_with_invalid_query(self, people_basic_query, test_data_path) -> None:
        """

        Test Loader With Invalid Query

        This method tests the behavior of the `Sqlite3DataLoader` class when provided with an invalid query. It verifies that the loader raises an `OperationalError` with the appropriate error
        * message.

        Parameters:
        - self: The instance of the test class.
        - people_basic_query: The invalid query string.
        - test_data_path: The relative path to the test database file.

        Return Type:
        - None

        Example Usage:
        test_loader_with_invalid_query(self, "SELECT * FROM people", "test_data")

        """
        valid_path = f"{Path.cwd()}\\{test_data_path}\\test_db1.db"
        invalid_query = people_basic_query
        valid_keys = ["start_date", "end_date", "car_id"]
        loader = Sqlite3DataLoader(valid_path, invalid_query, valid_keys)

        with pytest.raises(OperationalError) as e:
            loader.load()
        assert e.value.args[0] == "no such table: people"
