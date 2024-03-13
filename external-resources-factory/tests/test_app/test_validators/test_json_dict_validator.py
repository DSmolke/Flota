import pytest
from easyvalid_data_validator.customexceptions.array import InvalidArgumentType


class TestJsonDictValidator:
    """
    The `TestJsonDictValidator` class is used to test the `validate` method of the `JsonDictValidator` class.

    """
    class TestValidate:
        """
        The TestValidate class is used to test the functionality of the validate method in the MotValidator class. It contains two test methods:

        1. test_validate_with_all_data_correct:
            - Validates that the validate method returns the input data when all the data is correct.
            - Parameters:
                - mot_validator: An instance of the MotValidator class.
                - two_elements_valid_mot_data: A list of dictionaries containing valid MOT data.
            - Returns: None

        2. test_validate_with_one_data_incorrect:
            - Validates that the validate method raises an InvalidArgumentType exception when one of the data elements is incorrect.
            - Parameters:
                - mot_validator: An instance of the MotValidator class.
                - two_elements_valid_mot_data: A list of dictionaries containing valid MOT data.
            - Returns: None

        Note: This class does not include example code and does not use @author and @version tags.
        """
        def test_validate_with_all_data_correct(self, mot_validator, two_elements_valid_mot_data) -> None:
            """
            This method tests the `validate` method of the `mot_validator` object using the `two_elements_valid_mot_data` parameter.

            Parameters:
            - self: The instance of the class that the method belongs to.
            - mot_validator: The object that provides the `validate` method.
            - two_elements_valid_mot_data: The data that needs to be validated.

            Return type: None

            Example usage:
            test_validate_with_all_data_correct(self, mot_validator, two_elements_valid_mot_data)
            """
            assert mot_validator.validate(two_elements_valid_mot_data) == two_elements_valid_mot_data

        def test_validate_with_one_data_incorrect(self, mot_validator, two_elements_valid_mot_data) -> None:
            """
            Test method to validate the behavior of the `test_validate_with_one_data_incorrect` method.

            Args:
                self: The instance of the test class.
                mot_validator: The MOT validator object being tested.
                two_elements_valid_mot_data: List containing two elements of valid MOT data.

            Returns:
                None

            Raises:
                AssertionError: If the validation error is not raised or the error message is incorrect.
            """
            data = two_elements_valid_mot_data
            data.append(
                {
                    # invalid value in id
                    "mot_id": "1",
                    "start_date": "2022-03-15 00:00:00.000",
                    "end_date": "2023-03-15 00:00:00.000",
                    "car_id": 3
                }
            )
            with pytest.raises(InvalidArgumentType) as e:
                mot_validator.validate(two_elements_valid_mot_data)

            assert e.value.args[0] == 'Invalid value1 argument type'
