from pathlib import Path

from easyvalid_data_validator.constraints import Constraint

from app.factories.car_factories.csv_factories import FromCsvToCarsWithExpectedConstraintsDataFactory
from app.converters.to_car_converter import ToCarsConverter
from app.loaders.csv_loader import CsvDataLoader
from app.validators.json_dict_validator import JsonDictValidator


class TestFromCsvToCarsWithExpectedConstraintsDataFactory:
    """

    The TestFromCsvToCarsWithExpectedConstraintsDataFactory class is responsible for creating instances of data loader, validator, and converter for testing the transformation of data from
    * a CSV file to car objects with expected constraints.

    Attributes:
        - path (str): The path to the CSV file.
        - factory (FromCsvToCarsWithExpectedConstraintsDataFactory): An instance of the data factory with the specified constraints for car attributes.

    Methods:
        - test_create_loader(): This method tests the creation of a data loader instance and asserts that it is of type CsvDataLoader with the correct path.

        - test_create_validator(car_constraints): This method tests the creation of a validator instance and asserts that it is of type JsonDictValidator with the given car_constraints.

        - test_create_converter(): This method tests the creation of a converter instance and asserts that it is of type ToCarsConverter.

    """
    path = f"{Path.cwd()}\\data\\cars.csv"
    factory = FromCsvToCarsWithExpectedConstraintsDataFactory(f"{Path.cwd()}\\data\\cars.csv", {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}
    })

    def test_create_loader(self):
        """
        Test the create_data_loader method of the factory to ensure it returns the expected CsvDataLoader object.

        :param self: The current instance of the test case.
        :return: None

        Example usage:
        >> test = TestClass()
        >> test.test_create_loader()
        """
        assert self.factory.create_data_loader() == CsvDataLoader(self.path)

    def test_create_validator(self, car_constraints):
        """
        Test the create_validator method.

        This method tests whether the create_validator method of the factory correctly returns an instance of the JsonDictValidator class.

        Args:
            car_constraints (dict): The constraints for car objects, in JSON format.

        Raises:
            AssertionError: If the returned validator instance is not an instance of the JsonDictValidator class.

        Example:
            factory = ValidatorFactory()
            constraints = {
                "make": {"required": True},
                "model": {"required": True},
                "year": {"required": True, "type": "number"}
            }
            assert factory.test_create_validator(constraints) == JsonDictValidator(constraints)
        """
        assert self.factory.create_validator() == JsonDictValidator(car_constraints)

    def test_create_converter(self):
        """
        Test the create_converter method of the factory.

        This method verifies that the create_converter method of the factory returns an instance of the ToCarsConverter class.

        Parameters:
            self: The instance of the TestFactory class being tested.

        Returns:
            None.
        """
        assert type(self.factory.create_converter()) == type(ToCarsConverter())
