import os

APP = {
    'name': os.getenv('APP_NAME', 'Larapy'),
    'env': os.getenv('APP_ENV', 'production'),
    'debug': os.getenv('APP_DEBUG', 'false').lower() == 'true',
    'url': os.getenv('APP_URL', 'http://localhost'),
    'timezone': os.getenv('APP_TIMEZONE', 'UTC'),
    'locale': os.getenv('APP_LOCALE', 'en'),
    'fallback_locale': os.getenv('APP_FALLBACK_LOCALE', 'en'),
    'key': os.getenv('APP_KEY', ''),
}
