import os

EXCEPTIONS = {
    'dont_report': [
        'larapy.http.exceptions.NotFoundHttpException',
        'larapy.http.exceptions.MethodNotAllowedHttpException',
    ],
    
    'dont_flash': [
        'password',
        'password_confirmation',
        'token',
        'secret',
        'api_key',
        'api_secret',
        'private_key',
    ],
    
    'context': {
        'enabled': os.getenv('EXCEPTION_CONTEXT_ENABLED', 'true').lower() == 'true',
        'max_string_length': int(os.getenv('EXCEPTION_CONTEXT_MAX_STRING', '1000')),
        'max_array_items': int(os.getenv('EXCEPTION_CONTEXT_MAX_ARRAY', '50')),
    },
}
