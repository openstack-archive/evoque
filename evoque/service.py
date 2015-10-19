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

import logging
import multiprocessing

from oslo_config import cfg
from oslo_log import log

from evoque import opts

LOG = log.getLogger(__name__)


def prepare_service(args=None):
    conf = cfg.ConfigOpts()
    log.register_options(conf)

    # Register Evoque options
    for group, options in opts.list_opts():
        conf.register_opts(list(options),
                           group=None if group == "DEFAULT" else group)

    try:
        default_workers = multiprocessing.cpu_count() or 1
    except NotImplementedError:
        default_workers = 1

    conf.set_default("workers", default_workers, group="api")

    conf(args, project='evoque', validate_default_values=True)
    log.setup(conf, 'evoque')
    conf.log_opt_values(LOG, logging.DEBUG)

    return conf
