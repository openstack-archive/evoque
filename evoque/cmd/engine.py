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

"""Evoque engine service."""

import os
import uuid

from oslo_config import cfg
from oslo_log import log as logging
from oslo_service import service

from evoque.common import rpc_service
from evoque.engine.ticket import endpoint as ticket_endpoint
from evoque.i18n import _LI
from evoque import service as evoque_service

LOG = logging.getLogger(__name__)


def main():
    evoque_service.prepare_service()

    LOG.info(_LI('Starting evoque engine in PID %s') % os.getpid())

    conductor_id = str(uuid.uuid4())

    endpoints = [
        ticket_endpoint.Handler(),
    ]

    server = rpc_service.Service.create("evoque-engine",
                                        conductor_id, endpoints,
                                        binary='evoque-engine')
    launcher = service.launch(cfg.CONF, server)
    launcher.wait()
