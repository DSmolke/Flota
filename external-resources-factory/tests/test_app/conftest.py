import pytest
from easyquery_query_builder.queries.read_query_builder import ReadQueryBuilder
from easyvalid_data_validator.constraints import Constraint


@pytest.fixture(scope="session")
def car_constraints():
    """
    Returns the constraints for each attribute of a car.

    Returns:
        dict: A dictionary containing the constraints for each attribute of a car.

    Example:
        >>> constraints = car_constraints()
        >>> constraints
        {
            "id": {Constraint.INT_GRATER: 0},
            "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
            "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
            "brand": {Constraint.STRING_REGEX: r"^.*$"},
            "model": {Constraint.STRING_REGEX: r"^.*$"}
        }
    """
    return {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}
    }


@pytest.fixture(scope="session")
def mots_basic_query():
    """

    This method, `mots_basic_query`, is a fixture function that returns a parsed query.

    Parameters:
        None

    Returns:
        Parsed query: An object representing the parsed query.

    Example Usage:
        result = mots_basic_query()

    """
    return ReadQueryBuilder().add_select_statement('*').add_from_statement('mots').build().parse()


@pytest.fixture(scope="session")
def cars_basic_query():
    """

    cars_basic_query

    This method returns a parsed query that selects all columns from the 'cars' table.

    Returns:
        The parsed query as a string.

    """
    return ReadQueryBuilder().add_select_statement('*').add_from_statement('cars').build().parse()


@pytest.fixture(scope="session")
def people_basic_query():
    """

    This method, `people_basic_query`, is a fixture implemented using the pytest library in Python. It is used to return a query string that can be used to fetch basic information about
    * people from a database.

    Example usage:
    --------------
    ```python
    query = people_basic_query()
    # Execute the query...
    ```

    Returns:
    --------
    - str: A query string for fetching basic information about people.

    Note:
    -----
    - This method is implemented as a fixture, allowing it to be used by other test functions or fixtures in a pytest test suite.
    - The query string is generated using the `ReadQueryBuilder` class, which is responsible for constructing SQL queries.

    """
    return ReadQueryBuilder().add_select_statement('*').add_from_statement('people').build().parse()


@pytest.fixture(scope="session")
def car_keys():
    """
    Returns a list of car keys.

    The method returns a list of strings representing the keys of a car.
    The keys included in the list are "id", "registration_number",
    "first_registration_date", "vin", "brand", and "model".

    Returns:
        list: A list of strings representing the car keys.
    """
    return ["id", "registration_number", "first_registration_date", "vin", "brand", "model"]
