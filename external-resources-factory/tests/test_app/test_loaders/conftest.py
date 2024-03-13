import pytest
from easyquery_query_builder.queries.read_query_builder import ReadQueryBuilder
from easyvalid_data_validator.constraints import Constraint


@pytest.fixture
def test_data_path():
    """Set up test data path fixture.

    Returns:
        str: The path to the test data directory.
    """
    return 'tests\\test_data'



@pytest.fixture(scope="session")
def car_constraints():
    """
    car_constraints

    This method returns a dictionary that specifies the constraints for each field of a car object.

    Returns:
        dict: A dictionary specifying the constraints for each field of a car object. The keys of the dictionary are the field names, and the values are dictionaries specifying the constraints
    * for each field.

    Example:
        >>> car_constraints()
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
    This method, `mots_basic_query`, is a fixture function that returns a parsed query for selecting all columns from the 'mots' table.

    The function returns the result of parsing a query built using the `ReadQueryBuilder` class. The query includes a select statement with all columns specified and a from statement indicating
    * the table to select from.

    The returned query can be used for executing database retrieval operations.

    Example usage:
    query = mots_basic_query()
    # Execute the query and process the results

    """
    return ReadQueryBuilder().add_select_statement('*').add_from_statement('mots').build().parse()


@pytest.fixture(scope="session")
def cars_basic_query():
    """
    This method creates a query object using the ReadQueryBuilder class to construct a SELECT statement to retrieve all columns from the 'cars' table. The query is then built and parsed
    * to return the resulting query string.

    @return: A string representing the query.

    Example Usage:

        query = cars_basic_query()
        print(query) # SELECT * FROM cars

    """
    return ReadQueryBuilder().add_select_statement('*').add_from_statement('cars').build().parse()


@pytest.fixture(scope="session")
def people_basic_query():
    """
    Builds and parses a basic query for retrieving all columns from the 'people' table.

    Returns:
        A parsed query object.

    Example:
        query = people_basic_query()
        result = execute_query(query)
        # Process result...
    """
    return ReadQueryBuilder().add_select_statement('*').add_from_statement('people').build().parse()


@pytest.fixture(scope="session")
def car_keys():
    """

    Return a list of keys representing the attributes of a car.

    Returns:
        list: A list of strings representing the attributes of a car.

    """
    return ["id", "registration_number", "first_registration_date", "vin", "brand", "model"]

