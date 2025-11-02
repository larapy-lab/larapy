from larapy.database.migrations import Migration
from larapy.database.schema import Schema


class CreateFailedJobsTable(Migration):
    
    def up(self):
        Schema.create('failed_jobs', lambda table: (
            table.id(),
            table.string('uuid').unique(),
            table.text('connection'),
            table.text('queue'),
            table.long_text('payload'),
            table.long_text('exception'),
            table.timestamp('failed_at').use_current()
        ))
    
    def down(self):
        Schema.drop_if_exists('failed_jobs')
