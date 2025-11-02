from larapy.database.migrations import Migration
from larapy.database.schema import Schema


class CreateJobBatchesTable(Migration):
    
    def up(self):
        Schema.create('job_batches', lambda table: (
            table.string('id').primary(),
            table.string('name'),
            table.integer('total_jobs'),
            table.integer('pending_jobs'),
            table.integer('failed_jobs'),
            table.long_text('failed_job_ids'),
            table.text('options').nullable(),
            table.integer('cancelled_at').nullable(),
            table.integer('created_at'),
            table.integer('finished_at').nullable()
        ))
    
    def down(self):
        Schema.drop_if_exists('job_batches')
