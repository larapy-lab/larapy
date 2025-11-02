import os


def env(key: str, default=None):
    return os.environ.get(key, default)


QUEUE_CONFIG = {
    'default': env('QUEUE_CONNECTION', 'sync'),
    
    'connections': {
        'sync': {
            'driver': 'sync',
        },
        
        'database': {
            'driver': 'database',
            'table': 'jobs',
            'queue': 'default',
            'retry_after': 90,
        },
        
        'redis': {
            'driver': 'redis',
            'connection': 'default',
            'queue': env('REDIS_QUEUE', 'default'),
            'retry_after': 90,
            'block_for': None,
        },
    },
    
    'failed': {
        'driver': env('QUEUE_FAILED_DRIVER', 'database'),
        'database': env('DB_CONNECTION', 'sqlite'),
        'table': 'failed_jobs',
    },
    
    'batching': {
        'driver': 'database',
        'database': env('DB_CONNECTION', 'sqlite'),
        'table': 'job_batches',
    },
}
