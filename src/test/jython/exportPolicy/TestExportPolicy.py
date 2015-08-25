#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.xebialabs.deployit.engine.api import TaskBlockService
from exporter.modules.TaskExporter import TaskExporter

from org.mockito.Mockito import mock
from nose.tools import ok_

import os.path

class TestExportPolicy(object):

    def test_export_tasks_without_result(self):
        task_block_service = mock(TaskBlockService)
        exporter = TaskExporter(task_block_service, 30, "/tmp/output.csv")
        exporter.export()
        ok_(os.path.isfile("/tmp/output.csv"))