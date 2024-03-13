from pathlib import Path

from easyvalid_data_validator.constraints import Constraint

from app.factories.car_factories.jsonl_factories import FromJsonlToCarsWithExpectedConstraintsDataFactory
from app.converters.to_car_converter import ToCarsConverter
from app.loaders.jsonl_loader import JsonlDataLoader
from app.validators.json_dict_validator import JsonDictValidator


class TestFromJsonlFileToCarsWithExpectedConstraintsDataFactory:
    """

    TestFromJsonlFileToCarsWithExpectedConstraintsDataFactory

    This class represents a factory for creating data loaders, validators, and converters for JSONL files containing car data with expected constraints. It provides methods to test the creation
    * of these objects.

    Attributes:
    - path (str): The path of the JSONL file containing car data.

    Methods:
    - test_create_loader(): Tests the creation of a data loader for the JSONL file.
    - test_create_validator(car_constraints): Tests the creation of a validator for car data.
    - test_create_converter(): Tests the creation of a converter for car data.

    """
    path = f"{Path.cwd()}\\data\\cars.jsonl"
    factory = FromJsonlToCarsWithExpectedConstraintsDataFactory(f"{Path.cwd()}\\data\\cars.jsonl", {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}
    })

    def test_create_loader(self):
        """
        Tests the 'create_data_loader' method of the factory instance.

        This method asserts that the data loader created by the factory is of the expected type, i.e., 'JsonlDataLoader', with the given 'path' parameter.

        Parameters:
            self: The instance of the class being tested.

        Returns:
            None

        Example usage:
            factory = Factory()
            factory.path = "/path/to/file.jsonl"
            factory.test_create_loader()
        """
        assert self.factory.create_data_loader() == JsonlDataLoader(self.path)

    def test_create_validator(self, car_constraints):
        """
        Test the creation of a JSON dictionary validator with a given set of constraints.

        :param car_constraints: A dictionary containing the constraints for validating a car's properties.
        :type car_constraints: dict

        :return: None
        """
        assert self.factory.create_validator() == JsonDictValidator(car_constraints)

    def test_create_converter(self):
        """
        Test the create_converter method of the factory class.

        This method tests whether the create_converter method of the factory class returns an object of the same type as ToCarsConverter.

        Parameters:
            self : Factory
                The factory object on which the create_converter method is called.

        Returns:
            None
        """
        assert type(self.factory.create_converter()) == type(ToCarsConverter())
