from exporter.modules.TaskExporter import TaskExporter

task_exporter = TaskExporter(taskBlockService, job.days, job.targetFile, job.timePattern)
task_exporter.export()