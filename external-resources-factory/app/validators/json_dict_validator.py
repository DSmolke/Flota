from dataclasses import dataclass
from typing import Any

from easyvalid_data_validator.constraints import Constraint
from easyvalid_data_validator.validator import validate_json_data

from app.validators.validator import Validator


@dataclass
class JsonDictValidator(Validator):
    """
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
    constraints: dict[str, dict[Constraint, Any]]

    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """ Validates data using my validator package
        https://pypi.org/project/easyvalid-data-validator/
        """
        return [validate_json_data(element, self.constraints) for element in data]
