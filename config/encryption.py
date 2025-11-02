import os

ENCRYPTION = {
    'driver': os.getenv('ENCRYPTION_DRIVER', 'aes-256-cbc'),
    'key': os.getenv('APP_KEY', ''),
    'cipher': os.getenv('ENCRYPTION_CIPHER', 'aes-256-cbc'),
}
