from abc import abstractmethod, ABC
from dataclasses import dataclass


class FormFilesService(ABC):
    """
    This class `FormFilesService` is an abstract class that defines the interface for a service that handles form file uploads.

    Methods:
    ---------

    `get_upload_file_data(self) -> dict[str, bytes]`:
        This method is responsible for retrieving the uploaded file data from the form submission. It should return a dictionary with the file names as keys and the file data as values,
    * represented as bytes.

        Returns:
            A dictionary containing the uploaded file data. The keys are the file names, and the values are the file data as bytes.

        Raises:
            This method is an abstract method and must be implemented by any class that inherits from `FormFilesService`.
    """
    @abstractmethod
    def get_upload_file_data(self) -> dict[str, bytes]:
        """
            Gets the data of the uploaded file.

            :return: A dictionary with file data, where the keys are strings and the values are bytes.
        """
        pass


@dataclass(frozen=True)
class FormFilesServiceImpl(FormFilesService):
    """
    Service implementation for handling form files.

    :param file_path: The path to the file to be uploaded.
    :type file_path: str
    :param request_file_name: The name of the file in the request. Default is 'file'.
    :type request_file_name: str
    """
    file_path: str
    request_file_name: str = 'file'

    def get_upload_file_data(self) -> dict[str, bytes]:
        """
        Return the file data as a dictionary with the file name as key and the file content as value.

        :return: A dictionary with the file name as key and the file content as value.
        :rtype: dict[str, bytes]
        """
        return {
            f'{self.request_file_name}': open(self.file_path, 'rb')
        }
