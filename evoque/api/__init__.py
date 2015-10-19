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
from pecan import rest

from oslo_log import log

LOG = log.getLogger(__name__)


class TicketController(rest.RestController):

    @pecan.expose('json')
    def get(self):
        return {"version": "1.0.0"}


class V1Controller(object):

    def __init__(self):
        self.sub_controllers = {
            "status": TicketController(),
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


class RootController(object):
    v1 = V1Controller()

    @staticmethod
    @pecan.expose('json')
    def index():
        return {
            "versions": [{
                "status": "CURRENT",
                "links": [{
                    "rel": "self",
                    "href": pecan.request.application_url + "/v1/"
                }],
                "id": "v1.0",
                "updated": "2015-03-19"
            }]
        }
