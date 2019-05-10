#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
