# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from evoque.engine import workflow


class Handler(object):

    def __init__(self):
        super(Handler, self).__init__()
        self.workflow_driver = workflow.get_workflow()

    def workflow_create(self, context, name, wf_spec):
        workflow = self.workflow_driver.workflow_create(
            context, name, wf_spec)
        return {'workflow': workflow}

    def workflow_list(self, context):
        workflows = self.workflow_driver.workflow_list(
            context)
        return {'workflows': workflows}
