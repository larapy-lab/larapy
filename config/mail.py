from typing import Dict, Any


def get_config() -> Dict[str, Any]:
    return {
        'default': 'smtp',
        
        'mailers': {
            'smtp': {
                'transport': 'smtp',
                'host': 'localhost',
                'port': 587,
                'encryption': 'tls',
                'username': None,
                'password': None,
                'timeout': 30,
            },
            
            'ses': {
                'transport': 'ses',
            },
            
            'mailgun': {
                'transport': 'mailgun',
            },
            
            'postmark': {
                'transport': 'postmark',
            },
            
            'sendmail': {
                'transport': 'sendmail',
                'path': '/usr/sbin/sendmail -bs',
            },
            
            'log': {
                'transport': 'log',
                'channel': 'mail',
            },
            
            'array': {
                'transport': 'array',
            },
        },
        
        'from': {
            'address': 'hello@example.com',
            'name': 'Example App',
        },
    }
