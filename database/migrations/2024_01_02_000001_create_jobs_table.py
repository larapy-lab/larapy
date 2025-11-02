from larapy.database.migrations import Migration
from larapy.database.schema import Schema


class CreateJobsTable(Migration):
    
    def up(self):
        Schema.create('jobs', lambda table: (
            table.big_increments('id'),
            table.string('queue').index(),
            table.long_text('payload'),
            table.unsigned_tiny_integer('attempts'),
            table.unsigned_integer('reserved_at').nullable(),
            table.unsigned_integer('available_at'),
            table.unsigned_integer('created_at')
        ))
    
    def down(self):
        Schema.drop_if_exists('jobs')
