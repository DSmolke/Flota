from datetime import date

from app.converters.to_car_converter import ToCarsConverter
from app.models.car import Car


class TestToCarsConverter:
    """
    class TestToCarsConverter:
        def test_to_cars_converter(self, two_elements_valid_car_data) -> None:
            Converts a test case with car data into a list of Car objects.

            Parameters:
                two_elements_valid_car_data (list): A list containing two dictionaries of car data.

            Returns:
                None

            Raises:
                AssertionError: If the conversion does not result in the expected list of Car objects.
    """
    def test_to_cars_converter(self, two_elements_valid_car_data) -> None:
        """
        Converts a list of car data into a list of Car objects.

        Args:
            self: The object instance.
            two_elements_valid_car_data (List[Dict[str, Any]]): A list of car data, where each element is a dictionary
                containing the car information.

        Returns:
            None: This method does not return any value.

        Raises:
            AssertionError: If the converted list of Car objects is not equal to the expected list.

        Example:
            two_elements_valid_car_data = [
                {"make": "Toyota", "model": "Camry", "year": 2020},
                {"make": "Honda", "model": "Civic", "year": 2019}
            ]
            test_to_cars_converter(self, two_elements_valid_car_data)
        """
        assert ToCarsConverter().convert(two_elements_valid_car_data) == [
            Car(**two_elements_valid_car_data[0]), Car(**two_elements_valid_car_data[1])]
