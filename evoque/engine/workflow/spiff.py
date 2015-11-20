# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from evoque.db import api as db_api
from evoque.engine import workflow


class Workflow(workflow.Base):
    """Workflow engine powered by `SpiffWorkflow`

    https://github.com/knipknap/SpiffWorkflow
    """

    def __init__(self):
        super(Workflow, self).__init__()

    def workflow_create(self, context, name, wf_spec):
        """Create a workflow"""
        values = {
            'name': name,
            'spec': wf_spec
        }
        workflow = db_api.workflow_create(context, values)
        return workflow

    def workflow_list(self, context):
        workflows = db_api.workflow_get_all(context)
        return workflows
