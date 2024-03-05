from abc import ABC, abstractmethod
from dataclasses import dataclass

import httpx


class FileResourcer(ABC):
    """
    .. py:class:: FileResourcer(ABC)

        Abstract base class for file resource classes.

        .. py:method:: post_resource_to_api(files: dict[str, bytes]) -> str

            Sends files to an API.

            :param files: A dictionary containing file names as keys and file content as values.
            :type files: dict[str, bytes]
            :returns: A string representing the response from the API.
            :rtype: str
    """
    @abstractmethod
    def post_resource_to_api(self, files: dict[str, bytes]) -> str:
        """
        Submit a resource to the API via a POST request.

        :param files: A dictionary where keys are filenames and values are bytes representing file contents.
        :return: A string indicating the result of the request.
        """
        pass


@dataclass(frozen=True)
class FileResourcerImpl(FileResourcer):
    """A class for handling file resources and posting them to an API."""
    api_url: str

    def post_resource_to_api(self, files: dict[str, bytes]) -> str:
        """
        Posts the given files to the API endpoint and returns the URL of the resource.

        :param files: A dictionary containing the file names as keys and the file content as values.
                      The file content should be in bytes format.
        :return: The URL of the uploaded resource as a string.
        """
        response = httpx.post(self.api_url, files=files)
        return response.json().get('url')
