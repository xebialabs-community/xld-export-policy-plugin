#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from org.joda.time import LocalDate

class TaskExporter(object):
    def __init__(self, task_block_service, days, target_file, time_pattern = None, task_type = "DEPLOY"):
        self.task_block_service = task_block_service
        self.days = days
        self.target_file = target_file
        self.time_pattern = time_pattern
        self.task_type = task_type

    def export(self):
        now = LocalDate()
        tasks = self.task_block_service.export(now.minusDays(self.days),now)
        f = open(self.target_file, 'w')
        if self.task_type == "CONTROL":
            f.write("Starttime,TaskId,TaskName,controlTaskTargetCI,TaskType,User,Status,Endtime\n")
        if self.task_type == "DEPLOY":
            f.write("Starttime,TaskId,Version,Environment,DeployType,User,Status,Endtime\n")
        for task in tasks:
            if self.task_type == "CONTROL" and task.metadata["taskType"] in ("CONTROL", "INSPECTION"):
                f.write("%s,%s,%s,%s,%s,%s,%s,%s" % (task.startDate.toString(self.time_pattern), task.id, task.metadata["taskName"],task.metadata["controlTaskTargetCI"], task.metadata["taskType"],task.owner, task.state, task.completionDate.toString(self.time_pattern)))
                f.write("\n")
            if self.task_type == "DEPLOY" and task.metadata["taskType"] in ("ROLLBACK", "INITIAL", "UNDEPLOY", "UPGRADE"):
                f.write("%s,%s,%s/%s,%s,%s,%s,%s,%s" % (task.startDate.toString(self.time_pattern), task.id, task.metadata["application"],task.metadata["version"], task.metadata["environment_id"], task.metadata["taskType"],task.owner, task.state, task.completionDate.toString(self.time_pattern)))
                f.write("\n")
        f.close()