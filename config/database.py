"""Database configuration."""

database = {
    # Default database connection name
    'default': 'sqlite',
    
    # Migration configuration
    'migrations': {
        'path': 'database/migrations',
        'paths': ['database/migrations'],
        'table': 'migrations',
    },
    
    # Seeder configuration
    'seeders': {
        'path': 'database/seeders',
        'paths': ['database/seeders'],
    },
    
    # Database connections
    'connections': {
        'sqlite': {
            'driver': 'sqlite',
            'database': 'database/database.sqlite',
        },
        
        'mysql': {
            'driver': 'mysql',
            'host': '127.0.0.1',
            'port': 3306,
            'database': 'forge',
            'username': 'forge',
            'password': '',
            'charset': 'utf8mb4',
            'prefix': '',
        },
        
        'postgresql': {
            'driver': 'postgresql',
            'host': '127.0.0.1',
            'port': 5432,
            'database': 'forge',
            'username': 'forge',
            'password': '',
            'charset': 'utf8',
            'prefix': '',
            'schema': 'public',
        },
    },
}
