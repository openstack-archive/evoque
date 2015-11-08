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

from oslo_config import cfg


def list_opts():
    return [
        ("api", (
            cfg.PortOpt('port',
                        default=8888,
                        help='The port for the Evoque API server.'),
            cfg.StrOpt('host',
                       default='0.0.0.0',
                       help='The listen IP for the Evoque API server.'),
            cfg.BoolOpt('pecan_debug',
                        default=False,
                        help='Toggle Pecan Debug Middleware.'),
            cfg.IntOpt('workers', min=1,
                       help='Number of workers for Evoque API server. '
                       'By default the available number of CPU is used.'),
            cfg.IntOpt('max_limit',
                       default=1000,
                       help=('The maximum number of items returned in a '
                             'single response from a collection resource')),
        )),
        (None, (
            cfg.StrOpt('host',
                       default='0.0.0.0',
                       help='The listen IP for the Evoque engine server.'),
        )),
    ]
