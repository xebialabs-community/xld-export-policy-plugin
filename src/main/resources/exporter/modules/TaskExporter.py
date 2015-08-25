from org.joda.time import LocalDate

class TaskExporter(object):
    def __init__(self, task_block_service, days, target_file, time_pattern = None):
        self.task_block_service = task_block_service
        self.days = days
        self.target_file = target_file
        self.time_pattern = time_pattern

    def export(self):
        now = LocalDate()
        tasks = self.task_block_service.export(now.minusDays(self.days),now)
        f = open(self.target_file, 'w')
        f.write("Starttime,TaskId,Version,Environment,DeployType,User,Status,Endtime\n")
        for task in tasks:
            if task.metadata["taskType"] not in ("CONTROL", "INSPECTION"):
                f.write("%s,%s/%s,%s,%s,%s,%s,%s,%s" % (task.startDate.toString(self.time_pattern), task.id, task.metadata["application"],task.metadata["version"], task.metadata["environment_id"], task.metadata["taskType"],task.owner, task.state, task.completionDate.toString(self.time_pattern)))
                f.write("\n")
        f.close()