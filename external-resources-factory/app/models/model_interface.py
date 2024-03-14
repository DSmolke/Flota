from abc import ABC, abstractmethod
from typing import Any, Self


class ModelInterface(ABC):
    """

    Class: ModelInterface

    The ModelInterface class is an abstract base class (ABC) that provides the structure for implementing models. It defines two abstract methods that subclasses must implement: "as_dict
    *" and "from_dict".

    Methods:
    - as_dict: This abstract method is used to convert the model object into a dictionary representation. It should return a dictionary with keys and values representing the attributes of
    * the model object.

    - from_dict: This abstract class method is used to create a new instance of the model object from a dictionary representation. It takes a dictionary as input and should return a new
    * instance of the model object with attributes initialized from the dictionary values.

    """
    @abstractmethod
    def as_dict(self) -> dict[str, Any]:
        """
        Converts the current object into a dictionary representation.

        Returns:
            dict[str, Any]: A dictionary representation of the current object.

        """
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """Create an instance of the class from a dictionary.

        Args:
            data (dict): The dictionary containing the data to create the instance from.

        Returns:
            Self: An instance of the class.

        """
        pass
