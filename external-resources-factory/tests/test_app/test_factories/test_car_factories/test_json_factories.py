from pathlib import Path

from easyvalid_data_validator.constraints import Constraint

from app.factories.car_factories.json_factories import FromJsonFileToCarsWithExpectedConstraintsDataFactory
from app.converters.to_car_converter import ToCarsConverter
from app.loaders.json_loader import JsonDataLoader
from app.validators.json_dict_validator import JsonDictValidator


class TestFromJsonFileToCarsWithExpectedConstraintsDataFactory:
    """

    Class:
    TestFromJsonFileToCarsWithExpectedConstraintsDataFactory

    Description:
    This class is used for testing the TestFromJsonFileToCarsWithExpectedConstraintsDataFactory class.

    Attributes:
    - path (str): The path of the JSON file used for testing.
    - factory (FromJsonFileToCarsWithExpectedConstraintsDataFactory): An instance of the FromJsonFileToCarsWithExpectedConstraintsDataFactory class.

    Methods:
    - test_create_loader(): This method tests the creation of a data loader object and asserts that it is an instance of the JsonDataLoader class.
    - test_create_validator(car_constraints): This method tests the creation of a validator object and asserts that it is an instance of the JsonDictValidator class.
    - test_create_converter(): This method tests the creation of a converter object and asserts that it is an instance of the ToCarsConverter class.

    """
    path = f"{Path.cwd()}\\data\\cars.json"
    factory = FromJsonFileToCarsWithExpectedConstraintsDataFactory(f"{Path.cwd()}\\data\\cars.json", {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}
    })

    def test_create_loader(self):
        """
        Test the create_loader method of the factory class.

        This method tests whether the create_loader method of the factory class returns an instance of JsonDataLoader
        with the correct path.

        Parameters:
            - self: The instance of the test class.

        Returns:
            - None

        Raises:
            - AssertionError: If the create_loader method does not return an instance of JsonDataLoader with the correct path.
        """
        assert self.factory.create_data_loader() == JsonDataLoader(self.path)

    def test_create_validator(self, car_constraints):
        """
        Test if the factory correctly creates a JsonDictValidator given car_constraints.

        :param car_constraints: The constraints for validating a car.
        :type car_constraints: dict

        :return: None
        :rtype: None
        """
        assert self.factory.create_validator() == JsonDictValidator(car_constraints)

    def test_create_converter(self):
        """
        Test method for create_converter().

        This method tests if the create_converter() method of the factory class returns an object of the same type as the ToCarsConverter class.

        Returns:
            None

        """
        assert type(self.factory.create_converter()) == type(ToCarsConverter())
