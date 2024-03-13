from typing import Any

from app.factories.data_factory import DataFactory

class DataProcesor:
    """
    User has to provide DataFactory object. Then its create_data_loader, create_validator and create_converter will be
    assigned to data_loader, validator and converter params.
    """
    def __init__(self, data_factory: DataFactory) -> None:
        self.data_loader = data_factory.create_data_loader()
        self.validator = data_factory.create_validator()
        self.converter = data_factory.create_converter()

    def process(self) -> Any:
        """ Returns data processed by data_loader, validator and converter"""
        loaded_data = self.data_loader.load()
        validated_data = self.validator.validate(loaded_data)
        return self.converter.convert(validated_data)
