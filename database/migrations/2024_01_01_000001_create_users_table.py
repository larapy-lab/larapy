from larapy.database.migrations import Migration
from larapy.database.schema.schema import Schema, Blueprint


class CreateUsersTable(Migration):
    def up(self):
        schema = Schema(self._connection)
        
        def create_table(table: Blueprint):
            table.increments('id')
            table.string('name')
            table.string('email').unique()
            table.timestamp('email_verified_at').nullable()
            table.string('password')
            table.string('remember_token', 100).nullable()
            table.timestamps()
        
        schema.create('users', create_table)
    
    def down(self):
        schema = Schema(self._connection)
        schema.drop_if_exists('users')
