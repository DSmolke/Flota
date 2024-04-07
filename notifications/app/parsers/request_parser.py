from abc import ABC, abstractmethod
from typing import Any


class RequestParser(ABC):
    """
    An abstract class representing a request parser.

    Attributes:
        None

    Methods:
        parse: Abstract method to parse the input HTTP client and return a dictionary or a list of dictionaries.

    """
    @abstractmethod
    def parse(self, http_client) -> dict[str, Any] | list[dict[str, Any]]:
        """
        :param http_client: The HTTP client object used for making HTTP requests.
        :return: A dictionary or a list of dictionaries containing parsed data.
        """
        pass