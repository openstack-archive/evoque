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

from oslo_log import log
import pecan
import webob.exc
from werkzeug import serving

from evoque import exceptions
from evoque import service

LOG = log.getLogger(__name__)


PECAN_CONFIG = {
    'app': {
        'root': 'evoque.api.RootController',
        'modules': ['evoque.api'],
    },
}


class NotImplementedMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except exceptions.NotImplementedError:
            raise webob.exc.HTTPNotImplemented(
                "Sorry, this Evoque server does "
                "not implement this feature 😞")


def setup_app(config=PECAN_CONFIG, cfg=None):
    if cfg is None:
        raise RuntimeError("Config is actually mandatory")

    # NOTE(lawrancejing): pecan debug won't work in multi-process environment
    pecan_debug = cfg.api.pecan_debug
    if cfg.api.workers != 1 and pecan_debug:
        pecan_debug = False
        LOG.warning('pecan_debug cannot be enabled, if workers is > 1, '
                    'the value is overrided with False')

    app = pecan.make_app(
        config['app']['root'],
        debug=pecan_debug,
        guess_content_type_from_ext=False,
    )

    return app


class WerkzeugApp(object):
    # NOTE(lawrancejing): The purpose of this class is only to be used
    # with werkzeug to create the app after the werkzeug
    # fork gnocchi-api

    def __init__(self, conf):
        self.app = None
        self.conf = conf

    def __call__(self, environ, start_response):
        if self.app is None:
            self.app = setup_app(cfg=self.conf)
        return self.app(environ, start_response)


def build_server():
    conf = service.prepare_service()
    serving.run_simple(conf.api.host, conf.api.port,
                       WerkzeugApp(conf),
                       processes=conf.api.workers)
