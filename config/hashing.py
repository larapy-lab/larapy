import os

HASHING = {
    'driver': os.getenv('HASH_DRIVER', 'bcrypt'),
    
    'bcrypt': {
        'rounds': int(os.getenv('BCRYPT_ROUNDS', '12')),
    },
    
    'argon2': {
        'memory': int(os.getenv('ARGON2_MEMORY', '65536')),
        'time': int(os.getenv('ARGON2_TIME', '4')),
        'threads': int(os.getenv('ARGON2_THREADS', '1')),
    },
}
