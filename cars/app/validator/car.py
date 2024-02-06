from schemadict import schemadict

"""
car_schema implements .validate() method which will return error if any of dict keys won't meet declared constraints
"""
car_schema = schemadict({
    'registration': {
        'type': str,
        'min_len': 7,
        'max_len': 7,
        'regex': r'^[A-Z0-9]{7}$'
    },
    'vin': {
        'type': str,
        'min_len': 17,
        'max_len': 17,
        'regex': r'^[A-Z0-9]{17}$'
    },
    'make': {
        'type': str,
        'regex': r'^[A-Z]+( [A-Z]+)?$'
    },
    'model': {
        'type': str,
        'regex': r'^([A-Z0-9]+( [A-Z0-9]+)?)+$'
    },
    'first_registration_date': {
        'type': str,
        'min_len': 10,
        'max_len': 10
    },
    'production_year': {
        'type': str,
        'min_len': 4,
        'max_len': 4,
        'regex': r'^[0-9]{4}$'
    },
    'mileage': {
        'type': str,
        'min_len': 1,
        'max_len': 7,
        'regex': r'^\d+$'
    },
    'fuel_consumption': {
        'type': str,
        'min_len': 1,
        'max_len': 5,
        'regex': r'^\d+(([.,])\d{0,2})?$'
    },
    'fuel_type_id': {
        'type': int,
        '>=': 1,
        '<=': 3,
    },
    'vehicle_status_id': {
        'type': int,
        '>=': 1,
        '<=': 3
    }
})


