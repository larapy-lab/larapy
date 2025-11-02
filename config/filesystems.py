import os

FILESYSTEMS = {
    'default': os.getenv('FILESYSTEM_DISK', 'local'),
    
    'disks': {
        'local': {
            'driver': 'local',
            'root': os.getenv('FILESYSTEM_LOCAL_ROOT', 'storage/app'),
            'url': os.getenv('FILESYSTEM_LOCAL_URL', '/storage'),
            'visibility': 'public'
        },
        
        's3': {
            'driver': 's3',
            'key': os.getenv('AWS_ACCESS_KEY_ID'),
            'secret': os.getenv('AWS_SECRET_ACCESS_KEY'),
            'region': os.getenv('AWS_DEFAULT_REGION', 'us-east-1'),
            'bucket': os.getenv('AWS_BUCKET'),
            'url': os.getenv('AWS_URL'),
            'prefix': os.getenv('AWS_PREFIX', ''),
        },
        
        'gcs': {
            'driver': 'gcs',
            'project_id': os.getenv('GCS_PROJECT_ID'),
            'bucket': os.getenv('GCS_BUCKET'),
            'credentials': os.getenv('GCS_CREDENTIALS_PATH'),
        },
        
        'azure': {
            'driver': 'azure',
            'connection_string': os.getenv('AZURE_STORAGE_CONNECTION_STRING'),
            'container': os.getenv('AZURE_STORAGE_CONTAINER'),
        }
    }
}
