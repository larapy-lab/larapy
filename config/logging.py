import os

LOGGING = {
    'default': os.getenv('LOG_CHANNEL', 'stack'),
    
    'channels': {
        'stack': {
            'driver': 'stack',
            'channels': ['daily'],
            'ignore_exceptions': False,
        },
        
        'single': {
            'driver': 'file',
            'path': os.getenv('LOG_PATH', 'storage/logs/larapy.log'),
            'level': os.getenv('LOG_LEVEL', 'debug'),
        },
        
        'daily': {
            'driver': 'daily',
            'path': os.getenv('LOG_PATH', 'storage/logs/larapy.log'),
            'level': os.getenv('LOG_LEVEL', 'debug'),
            'days': int(os.getenv('LOG_DAILY_DAYS', '14')),
        },
        
        'stderr': {
            'driver': 'stream',
            'stream': 'stderr',
            'level': 'debug',
            'formatter': 'line',
        },
        
        'stdout': {
            'driver': 'stream',
            'stream': 'stdout',
            'level': 'debug',
            'formatter': 'line',
        },
        
        'null': {
            'driver': 'null',
        },
    },
}
