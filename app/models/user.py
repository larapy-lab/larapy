from larapy.database.orm import Model
from larapy.auth import Authenticatable
from larapy.hashing import Hash


class User(Model, Authenticatable):
    __table__ = 'users'
    
    fillable = ['name', 'email', 'password']
    hidden = ['password', 'remember_token']
    casts = {
        'email_verified_at': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
    }
    
    def set_password_attribute(self, value):
        self.attributes['password'] = Hash.make(value)
