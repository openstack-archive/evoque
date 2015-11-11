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

import pecan

from evoque.api.controllers.v1 import ticket
from evoque.api.controllers.v1 import workflow


class Controller(object):

    def __init__(self):
        self.sub_controllers = {
            "ticket": ticket.Controller(),
            "workflow": workflow.Controller(),
        }

        for name, ctrl in self.sub_controllers.items():
            setattr(self, name, ctrl)

    @pecan.expose('json')
    def index(self):
        return {
            "version": "1.0",
            "links": [
                {"rel": "self",
                 "href": pecan.request.application_url + "/v1"}
            ] + [
                {"rel": name,
                 "href": pecan.request.application_url + "/v1/" + name}
                for name in sorted(self.sub_controllers)
            ]
        }
