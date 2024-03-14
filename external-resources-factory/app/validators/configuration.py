from easyvalid_data_validator.constraints import Constraint

car_model_constraints = {
    'registration': {Constraint.IS_TYPE: str},
    'vin': {Constraint.IS_TYPE: str},
    'make': {Constraint.IS_TYPE: str},
    'model': {Constraint.IS_TYPE: str},
    'first_registration_date': {Constraint.IS_TYPE: str},
    'production_year': {Constraint.IS_TYPE: str},
    'mileage': {Constraint.IS_TYPE: str},
    'fuel_type_id': {Constraint.IS_TYPE: str},
    'vehicle_status_id': {Constraint.IS_TYPE: str},
    'fuel_consumption': {Constraint.IS_TYPE: str}
}

liability_model_constraints = {
    'legal_identifier': {Constraint.IS_TYPE: str},
    'start_date': {Constraint.IS_TYPE: str},
    'end_date': {Constraint.IS_TYPE: str},
    'car_registration_number': {Constraint.IS_TYPE: str},
    'active': {Constraint.IS_TYPE: str},
}
