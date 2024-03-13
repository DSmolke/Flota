from abc import ABC, abstractmethod

class DataFactory(ABC):
    """ Factory object abstraction that provides abstract methods: create_data_loader, create_validator, create_converter"""

    @abstractmethod
    def create_data_loader(self):
        """ Loader creation """
        pass

    @abstractmethod
    def create_validator(self):
        """ Validator creation """
        pass

    @abstractmethod
    def create_converter(self):
        """ Converter creation"""
        pass



