from dataclasses import dataclass
from typing import Any

from easyvalid_data_validator.constraints import Constraint

from app.factories.data_factory import DataFactory
from app.converters.to_liability_converter import ToLiabilityConverter
from app.loaders.csv_loader import CsvDataLoader
from app.validators.json_dict_validator import JsonDictValidator


@dataclass
class FromCsvToLiabilitiesWithExpectedConstraintsDataFactory(DataFactory):
    """
    path: path of csv file that has to load cars information

    constraints: dict that keys are names that will be validated and values are dict that has
        easyvalid_data_validator.constraints.Constraint objects as key and constraint (for example regex).
    Example of constraints dict:
    constraints = {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}

    csv_sep: has default value of ',', defines delimiter used in file
    """
    path: str
    constraints: dict[str, dict[Constraint, Any]]
    csv_sep: str = ','

    def create_data_loader(self):
        """ Creates CsvDataLoader using self.path and self.csv_sep """
        return CsvDataLoader(self.path, self.csv_sep)

    def create_validator(self):
        """ Creates JsonDictValidator using self. constraints """
        return JsonDictValidator(self.constraints)

    def create_converter(self):
        """ Creates ToCarsConverter """
        return ToLiabilityConverter()
