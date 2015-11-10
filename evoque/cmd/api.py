# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Evoque API service."""

import os
from werkzeug import serving

from oslo_config import cfg
from oslo_log import log as logging

from evoque.api import app as api_app
from evoque.common.i18n import _LI
from evoque.common import service

LOG = logging.getLogger(__name__)


class WerkzeugApp(object):
    # NOTE(lawrancejing): The purpose of this class is only to be used
    # with werkzeug to create the wsgi app

    def __init__(self, conf):
        self.app = None
        self.conf = conf

    def __call__(self, environ, start_response):
        if self.app is None:
            self.app = api_app.setup_app()
        return self.app(environ, start_response)


def main():
    service.prepare_service()

    LOG.info(_LI('Starting evoque api in PID %s') % os.getpid())

    serving.run_simple(cfg.CONF.api.host, cfg.CONF.api.port,
                       WerkzeugApp(cfg.CONF),
                       processes=cfg.CONF.api.workers)
