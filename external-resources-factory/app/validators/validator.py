from abc import ABC, abstractmethod
from typing import Any


class Validator(ABC):
    """
    Validator is an abstract base class that provides a template for implementing data validation.

    Methods
    -------
    validate(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        Validates the given data and returns a list of validated data.

    Example usage:
    ---------------
    class MyValidator(Validator):
        def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
            # Implement validation logic here
            ...

    my_validator = MyValidator()
    validated_data = my_validator.validate(data)
    """
    @abstractmethod
    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """

        Validate Method

        Parameters:
        - data: A list of dictionaries, where each dictionary represents a data entry.

        Returns:
        - A list of dictionaries, where each dictionary represents a validated data entry.

        """
        pass
