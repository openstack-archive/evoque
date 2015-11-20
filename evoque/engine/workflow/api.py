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

from evoque.common import rpc_service


class API(rpc_service.API):
    def __init__(self, transport=None, context=None, topic=None):
        super(API, self).__init__(transport, context,
                                  topic="evoque-engine")

    def workflow_create(self, name, wf_spec):
        return self._call('workflow_create', name=name, wf_spec=wf_spec)

    def workflow_list(self):
        return self._call('workflow_list')
