from larapy.database.migrations import Migration
from larapy.database.schema.schema import Schema, Blueprint


class CreatePasswordResetsTable(Migration):
    def up(self):
        schema = Schema(self._connection)
        
        def create_table(table: Blueprint):
            table.string('email')
            table.string('token')
            table.timestamp('created_at').nullable()
            table.index(['email'])
        
        schema.create('password_resets', create_table)
    
    def down(self):
        schema = Schema(self._connection)
        schema.drop_if_exists('password_resets')
