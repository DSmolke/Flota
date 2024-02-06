CORS_CONFIG = {
            'allow_headers': [
                'accept',
                'accept-encoding',
                'authorization',
                'content-type'
            ],
            'methods': [
                'delete',
                'get',
                'post',
                'patch',
                'put',
                'options'
            ],
            'origins': [
                'http://localhost:8000',
                'http://localhost:3000',
            ]
        }