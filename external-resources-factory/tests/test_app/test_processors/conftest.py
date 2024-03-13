from pathlib import Path

import pytest

from app.factories.car_factories.sqlite_factories import \
    FromSqlite3ToCarsWithExpectedConstraintsDataFactory

@pytest.fixture(scope="session")
def test_data_path():
    """Return the path to the test data folder.

    This method returns the path to the test data folder for the current test session.

    Returns:
        str: The path to the test data folder.

    Example usage:
        >>> test_data_path()
        'tests\\test_data'
    """
    return 'tests\\test_data'
@pytest.fixture(scope="session")
def test_db1_path(test_data_path):
    """Returns the absolute path to the test database file test_db1.db.

    Parameters:
    - test_data_path (str): The path to the test data directory.

    Returns:
    - str: The absolute path to the test database file test_db1.db.

    Example:
        test_data_path = "test_data"
        db1_path = test_db1_path(test_data_path)
        print(db1_path)
        # Output: C:\path\to\current\working\directory\test_data\test_db1.db
    """
    return f"{Path.cwd()}\\{test_data_path}\\test_db1.db"

@pytest.fixture(scope="session")
def cars_sql_factory(test_db1_path, car_constraints, cars_basic_query, car_keys):
    """

    This method `cars_sql_factory` is a fixture function that initializes and returns an instance of the `FromSqlite3ToCarsWithExpectedConstraintsDataFactory` class. It takes four parameters
    * as input: `test_db1_path`, `car_constraints`, `cars_basic_query`, and `car_keys`. The fixture function is used in the context of session scope.

    Parameters:
    - `test_db1_path` (str): The path to the test SQLite database file.
    - `car_constraints` (list): A list of car constraints.
    - `cars_basic_query` (str): The basic query for retrieving car data.
    - `car_keys` (list): A list of car keys.

    Returns:
    - An instance of the `FromSqlite3ToCarsWithExpectedConstraintsDataFactory` class.

    """
    return FromSqlite3ToCarsWithExpectedConstraintsDataFactory(test_db1_path, car_constraints, cars_basic_query,
                                                               car_keys)
