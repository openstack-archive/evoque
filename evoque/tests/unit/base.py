# Copyright 2010-2011 OpenStack Foundation
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
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

import copy

import mock
from oslo_config import cfg
from oslo_log import log
from oslotest import base
import pecan
import testscenarios

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


class TestCase(base.BaseTestCase):
    """Test case base class for all unit tests."""

    def setUp(self):
        super(TestCase, self).setUp()
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

        def make_context(*args, **kwargs):
            # If context hasn't been constructed with token_info
            if not kwargs.get('auth_token_info'):
                kwargs['auth_token_info'] = copy.deepcopy(token_info)
            if not kwargs.get('project_id'):
                kwargs['project_id'] = 'fake_project'
            if not kwargs.get('user_id'):
                kwargs['user_id'] = 'fake_user'

            context = evoque_context.RequestContext(*args, **kwargs)
            return evoque_context.RequestContext.from_dict(context.to_dict())

        p = mock.patch.object(evoque_context, 'make_context',
                              side_effect=make_context)
        self.mock_make_context = p.start()
        self.addCleanup(p.stop)

        self.useFixture(fixture.ConfigFixture())

        def reset_pecan():
            pecan.set_config({}, overwrite=True)

        self.addCleanup(reset_pecan)

    def config(self, **kw):
        """Override config options for a test."""
        group = kw.pop('group', None)
        for k, v in kw.items():
            CONF.set_override(k, v, group)
