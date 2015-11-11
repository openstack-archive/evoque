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

import testscenarios

from oslo_config import cfg
from oslo_log import log
from oslotest import base

from evoque.common import context as evoque_context
from evoque.tests.unit import fixture

CONF = cfg.CONF
log.register_options(CONF)
CONF.set_override('use_stderr', False)


class BaseTestCase(testscenarios.WithScenarios, base.BaseTestCase):
    """Test base class."""

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.addCleanup(cfg.CONF.reset)


class DBTestCase(base.BaseTestCase):
    """Test case base class for all unit tests."""

    def setUp(self):
        super(DBTestCase, self).setUp()
        self.useFixture(fixture.DBTestFixture())

        token_info = {
            'token': {
                'project': {
                    'id': 'fake_project'
                },
                'user': {
                    'id': 'fake_user'
                }
            }
        }
        self.context = evoque_context.RequestContext(
            auth_token_info=token_info,
            project_id='fake_project',
            user_id='fake_user')
