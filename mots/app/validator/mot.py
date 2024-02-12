from schemadict import schemadict

"""
mot_schema implements .validate() method which will return error if any of dict keys won't meet declared constraints
"""

mot_schema = schemadict({
    'legal_identifier': {
        'type': str,
        'min_len': 20,
        'max_len': 25
    },
    'start_date': {
        'type': str,
        'min_len': 10,
        'max_len': 10
    },
    'end_date': {
        'type': str,
        'min_len': 10,
        'max_len': 10
    },
    'car_registration_number': {
        'type': str,
        'min_len': 7,
        'max_len': 7,
        'regex': r'^[A-Z0-9]{7}$'
    },
    'img_url': {
        'type': str,
        'regex': r'https://[^\s]+'
    },
    'active': {
        'type': bool
    },
})
