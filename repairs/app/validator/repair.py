from schemadict import schemadict

"""
repair_schema implements .validate() method which will return error if any of dict keys won't meet declared constraints
"""

repair_schema = schemadict({
    'car_id': {
        'type': int,
    },
    'repair_status': {
        'type': int,
        '>=': 1,
        '<=': 3
    },
    'repair_description': {
        'type': str,
        'min_len': 1,
        'max_len': 500
    },
    'approximate_duration': {
        'type': int,
        '>=': 1,
        '<=': 360,
    },
    'start_date': {
        'type': str,
        'regex': r'^\d{4}-\d{2}-\d{2}$'
    },
    'garage_name': {
        'type': str,
        'min_len': 1,
        'max_len': 100
    },
    'garage_phone': {
        'type': str,
        'min_len': 1,
        'max_len': 13
    },
})
