from pathlib import Path

from easyvalid_data_validator.constraints import Constraint

from app.factories.car_factories.txt_factories import FromTxtToCarsWithExpectedConstraintsDataFactory
from app.converters.to_car_converter import ToCarsConverter
from app.loaders.txt_loader import TxtDataLoader
from app.validators.json_dict_validator import JsonDictValidator


class TestFromTxtToCarsWithExpectedConstraintsDataFactory:
    """
    Class: TestFromTxtToCarsWithExpectedConstraintsDataFactory

    This class is responsible for unit testing the methods of the FromTxtToCarsWithExpectedConstraintsDataFactory class.

    Attributes:
    - path: A string representing the path to the cars.txt file.
    - factory: An instance of the FromTxtToCarsWithExpectedConstraintsDataFactory class.

    Methods:
    - test_create_loader(): Tests whether the create_data_loader() method of the factory object returns an instance of the TxtDataLoader class.
    - test_create_validator(car_constraints): Tests whether the create_validator() method of the factory object returns an instance of the JsonDictValidator class with the given car_constraints
    *.
    - test_create_converter(): Tests whether the create_converter() method of the factory object returns an instance of the ToCarsConverter class.

    No example code provided.
    """
    path = f"{Path.cwd()}\\data\\cars.txt"
    factory = FromTxtToCarsWithExpectedConstraintsDataFactory(f"{Path.cwd()}\\data\\cars.txt", {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}
    })

    def test_create_loader(self):
        """
        Test method for creating a data loader from a factory.

        :returns: None
        """
        assert self.factory.create_data_loader() == TxtDataLoader(self.path)

    def test_create_validator(self, car_constraints):
        """
        Test the creation of a validator using the factory method.

        Parameters:
        - car_constraints: The constraints to be used in the creation.

        Returns:
        - None

        Example Usage:
        test_create_validator({"model": {"type": "string", "required": True}, "year": {"type": "integer", "min": 1900, "max": 2021}})
        """
        assert self.factory.create_validator() == JsonDictValidator(car_constraints)

    def test_create_converter(self):
        """
        Test the create_converter method of the factory.

        This method tests whether the create_converter method of the factory returns an instance of a converter class.

        :param self: The instance of the test case.
        :type self: object

        :return: None
        """
        assert type(self.factory.create_converter()) == type(ToCarsConverter())
