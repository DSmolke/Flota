from pathlib import Path

from easyvalid_data_validator.constraints import Constraint

from app.factories.car_factories.xlsx_factories import FromXlsxToCarsWithExpectedConstraintsDataFactory
from app.converters.to_car_converter import ToCarsConverter
from app.loaders.xlsx_loader import XlsxDataLoader
from app.validators.json_dict_validator import JsonDictValidator


class TestFromXlsxToCarsWithExpectedConstraintsDataFactory:
    """
    Class: TestFromXlsxToCarsWithExpectedConstraintsDataFactory

    This class is a test factory for creating objects related to converting data from an Xlsx file to Car objects with expected constraints.

    Attributes:
    - path: A string representing the path to the Xlsx file containing the data.
    - factory: An instance of FromXlsxToCarsWithExpectedConstraintsDataFactory initialized with the path and a dictionary of constraints for each attribute of the Car object.

    Methods:
    - test_create_loader(): This method tests the creation of a data loader object. It asserts that the created object is an instance of XlsxDataLoader and its path matches the attribute
    * 'path'.
    - test_create_validator(car_constraints): This method tests the creation of a validator object. It asserts that the created object is an instance of JsonDictValidator and its constraints
    * match the provided 'car_constraints' parameter.
    - test_create_converter(): This method tests the creation of a converter object. It asserts that the created object is an instance of ToCarsConverter.

    """
    path = f"{Path.cwd()}\\data\\cars.xlsx"
    factory = FromXlsxToCarsWithExpectedConstraintsDataFactory(f"{Path.cwd()}\\data\\cars.xlsx", {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}
    })

    def test_create_loader(self):
        """
        This method tests the create_data_loader() method of the factory object.

        Parameters:
        - self: the reference to the current instance of the class (implicit parameter)

        Return type:
        - None

        Example usage:
        test_create_loader()

        """
        assert self.factory.create_data_loader() == XlsxDataLoader(self.path)

    def test_create_validator(self, car_constraints):
        """
        Test the create_validator method.

        Args:
            self (object): The instance of the class on which the method is called.
            car_constraints (dict): The constraints for the car.

        Returns:
            None

        Raises:
            AssertionError: If the created validator is not an instance of JsonDictValidator.

        Example:
            To test the create_validator method, we can use the following code snippet:

                car_constraints = {...}  # Replace with actual constraints
                self.test_create_validator(car_constraints)

                # Assert that the created validator is an instance of JsonDictValidator
                assert isinstance(self.factory.create_validator(), JsonDictValidator)
        """
        assert self.factory.create_validator() == JsonDictValidator(car_constraints)

    def test_create_converter(self):
        """
        This method tests the create_converter method of the factory class.

        Parameters:
        self (object): The instance of the test class.

        Returns:
        None

        """
        assert type(self.factory.create_converter()) == type(ToCarsConverter())
