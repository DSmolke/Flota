import os
from abc import abstractmethod, ABC
from dataclasses import dataclass


class FileCatalogService(ABC):
    """
    FileCatalogService is an abstract base class for a file catalog service.

    Attributes:
        None

    Methods:
        get_current_file_path()
        delete_all_files()
    """
    @abstractmethod
    def get_current_file_path(self) -> str:
        """
        Returns the current file path.

        :return: The current file path.
        :rtype: str
        """
        pass

    @abstractmethod
    def delete_all_files(self) -> None:
        """
        Deletes all files in the current directory.

        :return: None
        """
        pass


@dataclass(frozen=True)
class FileCatalogServiceImpl(FileCatalogService):
    """
    This class provides an implementation of the FileCatalogService interface. It allows managing files in a catalog located at a specific path.

    :class: `FileCatalogServiceImpl` extends :class: `FileCatalogService`.

    Attributes:
        catalog_path (str): The path to the catalog where files are stored.

    Methods:
        - :func: `get_current_file_path`: Returns the path of the current file in the catalog.
        - :func: `delete_all_files`: Deletes all files in the catalog.
        - :func: `_get_all_files`: Returns a list of all files in the catalog.

    """
    catalog_path: str

    def get_current_file_path(self) -> str:
        """
        Returns the current file path.

        :return: The current file path.
        :rtype: str
        """
        if len(self._get_all_files()) > 1:
            raise ValueError('Too many files')

        while len(self._get_all_files()) == 0:
            pass
        while ''.join(self._get_all_files()).endswith('.crdownload'):
            pass
        files = self._get_all_files()

        return os.path.join(self.catalog_path, files[0])

    def delete_all_files(self) -> None:
        """
        Deletes all files in the catalog directory.

        :return: None
        """
        for file in self._get_all_files():
            file_path = os.path.join(self.catalog_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def _get_all_files(self) -> list[str]:
        """Get the list of all files in the specified catalog.

        :return: A list of strings representing the file names.
        :rtype: list[str]
        """
        files = os.listdir(self.catalog_path)
        return files
