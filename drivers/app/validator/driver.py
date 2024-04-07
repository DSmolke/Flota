from schemadict import schemadict

"""
driver_schema implements .validate() method which will return error if any of dict keys won't meet declared constraints
"""

driver_schema = schemadict({
    'first_name': {
        'type': str,
        'max_len': 50
    },
    'last_name': {
        'type': str,
        'max_len': 50
    },
    'phone_number': {
        'type': str,
        'max_len': 9
    },
    'email': {
        'type': str,
        'max_len': 500,
        'regex': r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    },
    'car_registration': {
        'type': str,
        'regex': r'^[A-Z0-9]{7}$',
        'max_len': 7
    }
})
