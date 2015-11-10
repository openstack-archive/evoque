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

import multiprocessing
import socket

from oslo_config import cfg

from evoque.common.i18n import _


try:
    default_workers = multiprocessing.cpu_count() or 1
except NotImplementedError:
    default_workers = 1


def list_opts():
    return [
        ("api", (
            cfg.PortOpt('port',
                        default=8888,
                        help=_('The port for the Evoque API server.')),
            cfg.StrOpt('host',
                       default='0.0.0.0',
                       help=_('The listen IP for the Evoque API server.')),
            cfg.BoolOpt('pecan_debug',
                        default=False,
                        help=_('Toggle Pecan Debug Middleware.')),
            cfg.IntOpt('workers', default=default_workers,
                       help=_('Number of workers for Evoque API server.')),
            cfg.IntOpt('max_limit',
                       default=1000,
                       help=_('The maximum number of items returned in a '
                              'single response from a collection resource')),
            cfg.BoolOpt('enable_authentication',
                        default=True,
                        help=_('This option enables or disables user '
                               'authentication via Keystone. '
                               'Default value is True.')),
        )),
        ("DEFAULT", (
            cfg.StrOpt('host',
                       default=socket.getfqdn(),
                       help=_('The listen IP for the Evoque engine server.')),
        )),
    ]
