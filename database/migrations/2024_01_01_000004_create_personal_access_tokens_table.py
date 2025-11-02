from larapy.database.migrations import Migration
from larapy.database.schema import Schema, Blueprint


class CreatePersonalAccessTokensTable(Migration):
    def up(self):
        schema = Schema(self._connection)
        
        def create_table(table: Blueprint):
            table.id()
            table.morph('tokenable')
            table.string('name')
            table.string('token', 64).unique()
            table.text('abilities').nullable()
            table.timestamp('last_used_at').nullable()
            table.timestamp('expires_at').nullable()
            table.timestamps()
        
        schema.create('personal_access_tokens', create_table)
    
    def down(self):
        schema = Schema(self._connection)
        schema.drop_if_exists('personal_access_tokens')
