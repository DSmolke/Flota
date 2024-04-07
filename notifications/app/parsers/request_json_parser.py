from dataclasses import dataclass
from typing import Any

from app.parsers.request_parser import RequestParser


@dataclass
class RequestJsonParser(RequestParser):
    """

    RequestJsonParser Class Documentation
    -------------------------------------

    This class is responsible for parsing JSON responses obtained from an HTTP service.

    Attributes:
        url (str): The URL to request the JSON data from.
        param (str | None): The parameter to extract from the JSON data. If None, the entire JSON response is returned.

    Methods:
        parse(http_client) -> dict[str, Any] | list[dict[str, Any]]:
            This method sends an HTTP GET request to the specified URL using the provided HTTP client.

            Args:
                http_client: An instance of an HTTP client used to make the request.

            Returns:
                If the `param` attribute is not None, the method returns the value of the specified parameter from the JSON response,
                otherwise it returns the entire JSON response as a dictionary or a list of dictionaries.


    """
    url: str
    param: str | None

    def parse(self, http_client) -> dict[str, Any] | list[dict[str, Any]]:
        """
        Parses the response from an HTTP client and returns the extracted data.

        :param http_client: The HTTP client object used to make the request.
        :return: The extracted data as a dictionary or a list of dictionaries.
        """
        if self.param:
            return http_client.get(self.url).json()[self.param]
        return http_client.get(self.url).json()