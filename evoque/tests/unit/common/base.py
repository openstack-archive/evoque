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

import logging
import os

import fixtures
import testscenarios
import testtools


TEST_DEFAULT_LOGLEVELS = {'migrate': logging.WARN,
                          'sqlalchemy': logging.WARN}
_LOG_FORMAT = "%(levelname)8s [%(name)s] %(message)s"
_TRUE_VALUES = ('True', 'true', '1', 'yes')


class FakeLogMixin(object):
    def setup_logging(self):
        # Assign default logs to self.LOG so we can still
        # assert on evoque logs.
        default_level = logging.INFO
        if os.environ.get('OS_DEBUG') in _TRUE_VALUES:
            default_level = logging.DEBUG

        self.LOG = self.useFixture(
            fixtures.FakeLogger(level=default_level, format=_LOG_FORMAT))
        base_list = set([nlog.split('.')[0]
                         for nlog in logging.Logger.manager.loggerDict])
        for base in base_list:
            if base in TEST_DEFAULT_LOGLEVELS:
                self.useFixture(fixtures.FakeLogger(
                    level=TEST_DEFAULT_LOGLEVELS[base],
                    name=base, format=_LOG_FORMAT))
            elif base != 'evoque':
                self.useFixture(fixtures.FakeLogger(
                    name=base, format=_LOG_FORMAT))


class EvoqueTestCase(testscenarios.WithScenarios,
                     testtools.TestCase, FakeLogMixin):

    TIME_STEP = 0.1

    def setUp(self):
        super(EvoqueTestCase, self).setUp()
        self.setup_logging()
