from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.resources.file_resourcer import FileResourcer
from app.resources.form_files_service import FormFilesService


class CarReportManager(ABC):
    """This is the documentation for the CarReportManager class.

    The CarReportManager class is an abstract base class (ABC) that provides a method for persisting car reports and retrieving the URL where the report is stored.

    Attributes:
        None

    Methods:
        persist_car_report_and_get_url: Persists the car report and returns the URL where the report is stored.

    """
    @abstractmethod
    def persist_car_report_and_get_url(self) -> str:
        """
        Save the car report and return the URL.

        :return: A string representing the URL of the saved car report.
        """
        pass


@dataclass(frozen=True)
class CarReportManagerImpl(CarReportManager):
    """

    CarReportManagerImpl Class
    --------------------------

    This class implements the `CarReportManager` interface and provides functionality to persist a car report and obtain the URL of the persisted file.

    Methods
    -------
    persist_car_report_and_get_url()
        Persists a car report file and returns the URL of the persisted file.

    Attributes
    ----------
    form_files_service : FormFilesService
        The service for handling form files.
    file_resourcer : FileResourcer
        The resource manager for handling file resources.

    """
    form_files_service: FormFilesService
    file_resourcer: FileResourcer

    def persist_car_report_and_get_url(self) -> str:
        """
        Persists the car report and retrieves the URL of the persisted file.

        :return: The URL of the persisted car report file.
        """
        data = self.form_files_service.get_upload_file_data()
        file_url = self.file_resourcer.post_resource_to_api(data)
        return file_url
