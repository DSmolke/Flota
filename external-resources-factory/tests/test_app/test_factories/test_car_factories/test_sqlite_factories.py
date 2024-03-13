from pathlib import Path

from easyquery_query_builder.queries.read_query_builder import ReadQueryBuilder
from easyvalid_data_validator.constraints import Constraint

from app.factories.car_factories.sqlite_factories import FromSqlite3ToCarsWithExpectedConstraintsDataFactory
from app.converters.to_car_converter import ToCarsConverter
from app.loaders.sqlite_loader import Sqlite3DataLoader
from app.validators.json_dict_validator import JsonDictValidator


class TestFromSqlite3ToCarsWithExpectedConstraintsDataFactory:
    """

    Docstring for class TestFromSqlite3ToCarsWithExpectedConstraintsDataFactory:

    This class represents a test suite for the FromSqlite3ToCarsWithExpectedConstraintsDataFactory class. It contains methods to test the various functionalities of the factory.

    Attributes:
    - path: The path to the SQLite3 database file.
    - keys: The list of keys/columns to retrieve from the database.
    - query: The SQL query to retrieve the data from the database.
    - factory: An instance of the FromSqlite3ToCarsWithExpectedConstraintsDataFactory class.

    Methods:
    - test_create_loader: Tests the creation of a data loader instance using the factory.
    - test_create_validator: Tests the creation of a validator instance using the factory.
    - test_create_converter: Tests the creation of a converter instance using the factory.



    """
    path = f"{Path.cwd()}\\data\\test_db1.db"
    keys = ["id", "registration_number", "first_registration", "brand", "model"]
    query = ReadQueryBuilder().add_select_statement('*').add_from_statement('cars').build().parse()
    factory = FromSqlite3ToCarsWithExpectedConstraintsDataFactory(
        f"{Path.cwd()}\\data\\test_db1.db",
        {
            "id": {Constraint.INT_GRATER: 0},
            "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
            "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
            "brand": {Constraint.STRING_REGEX: r"^.*$"},
            "model": {Constraint.STRING_REGEX: r"^.*$"}
        },
        ReadQueryBuilder().add_select_statement('*').add_from_statement('cars').build().parse(),
        ["id", "registration_number", "first_registration", "brand", "model"]
    )

    def test_create_loader(self):
        """
        Test the create_loader method.

        This method tests the create_loader method of the factory class. It creates a test loader and a twin loader
        using the create_data_loader method of the factory class. It then asserts that the path, query, and keys of
        the test loader are equal to the path, query, and keys of the twin loader.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        test_loader = self.factory.create_data_loader()
        twin_loader = Sqlite3DataLoader(self.path, self.query, self.keys)
        assert test_loader.path == twin_loader.path
        assert test_loader.query == twin_loader.query
        assert test_loader.keys == twin_loader.keys

    def test_create_validator(self, car_constraints):
        """
        Test method to create a validator and compare it with the expected constraints.

        Parameters:
        car_constraints (dict): A dictionary containing the constraints for cars.

        Returns:
        None

        """
        test_validator = self.factory.create_validator()
        twin_validator = JsonDictValidator(car_constraints)

        assert test_validator.constraints == twin_validator.constraints

    def test_create_converter(self):
        """
        Test case for the create_converter method.

        This method tests the create_converter method of the factory object.
        It verifies that the created converter object is equal to the expected converter object.

        Parameters:
            self (obj): The instance of the current test class.

        Returns:
            None
        """
        test_converter = self.factory.create_converter()
        twin_converter = ToCarsConverter()

        assert test_converter == twin_converter
