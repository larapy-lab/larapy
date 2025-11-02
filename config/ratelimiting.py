import os

RATE_LIMITING = {
    'default': 'api',
    
    'limiters': {
        'api': {
            'max_attempts': int(os.getenv('RATE_LIMIT_API', '60')),
            'decay_minutes': 1,
        },
        
        'auth': {
            'max_attempts': 5,
            'decay_minutes': 1,
        },
        
        'global': {
            'max_attempts': 1000,
            'decay_minutes': 1,
        },
    },
    
    'headers': {
        'limit': 'X-RateLimit-Limit',
        'remaining': 'X-RateLimit-Remaining',
        'retry_after': 'Retry-After',
        'reset': 'X-RateLimit-Reset',
    },
}
