#!/usr/bin/env python
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Evoque Engine Server.
"""

import eventlet
eventlet.monkey_patch()

import os
import sys

# If ../evoque/__init__.py exists, add ../ to Python search path, so that
# it will override what happens to be installed in /usr/(local/)lib/python...
POSSIBLE_TOPDIR = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir))
if os.path.exists(os.path.join(POSSIBLE_TOPDIR, 'evoque', '__init__.py')):
    sys.path.insert(0, POSSIBLE_TOPDIR)

from oslo_config import cfg
from oslo_i18n import _lazy
from oslo_log import log as logging
from oslo_service import service

from evoque.common import consts
from evoque.common import messaging
from evoque import opts

_lazy.enable_lazy()

LOG = logging.getLogger('evoque.engine')


def main():
    conf = cfg.ConfigOpts()

    # Register Evoque options
    for group, options in opts.list_opts():
        conf.register_opts(list(options),
                           group=None if group == "DEFAULT" else group)

    logging.register_options(cfg.CONF)
    cfg.CONF(project='evoque', prog='evoque-engine')
    logging.setup(cfg.CONF, 'evoque-engine')
    logging.set_defaults()
    messaging.setup()

    from evoque.engine import service as engine

    srv = engine.EngineService(conf.host, consts.ENGINE_TOPIC)
    launcher = service.launch(cfg.CONF, srv,
                              workers=1)
    # the following periodic tasks are intended serve as HA checking
    # srv.create_periodic_tasks()
    launcher.wait()
