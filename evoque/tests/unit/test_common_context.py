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

from evoque.common import context
from evoque.tests.unit.common import base


class TestRequestContext(base.EvoqueTestCase):

    def setUp(self):
        self.ctx = {
            'auth_token': '123',
            'auth_url': 'http://xyz',
            'domain_id': 'domain-id',
            'domain_name': 'domain-name',
            'user_name': 'mick',
            'user_id': 'user-id',
            'project_name': 'a project',
            'project_id': 'project-id',
            'roles': ['arole', 'notadmin'],
            'is_admin': False,
            'read_only': False,
            'show_deleted': False,
            'trust_id': "trust-id",
            'auth_token_info': {'123info': 'woop'},
            'all_tenants': False,
        }

        super(TestRequestContext, self).setUp()

    def test_request_context_init(self):
        ctx = context.RequestContext(
            auth_token=self.ctx.get('auth_token'),
            auth_url=self.ctx.get('auth_url'),
            domain_id=self.ctx.get('domain_id'),
            domain_name=self.ctx.get('domain_name'),
            user_name=self.ctx.get('user_name'),
            user_id=self.ctx.get('user_id'),
            project_domain=self.ctx.get('project_domain'),
            project_name=self.ctx.get('project_name'),
            project_id=self.ctx.get('project_id'),
            roles=self.ctx.get('roles'),
            is_admin=self.ctx.get('is_admin'),
            read_only=self.ctx.get('read_only'),
            show_deleted=self.ctx.get('show_deleted'),
            trust_id=self.ctx.get('trust_id'),
            auth_token_info=self.ctx.get('auth_token_info'),
            all_tenants=self.ctx.get('all_tenants'))

        ctx_dict = ctx.to_dict()
        del(ctx_dict['request_id'])
        del(ctx_dict['user'])
        del(ctx_dict['domain'])
        del(ctx_dict['user_domain'])
        del(ctx_dict['user_identity'])
        del(ctx_dict['resource_uuid'])
        del(ctx_dict['project_domain'])
        del(ctx_dict['tenant'])
        self.assertEqual(self.ctx, ctx_dict)

    def test_request_context_from_dict(self):
        ctx = context.RequestContext.from_dict(self.ctx)
        ctx_dict = ctx.to_dict()
        del(ctx_dict['request_id'])
        del(ctx_dict['user'])
        del(ctx_dict['domain'])
        del(ctx_dict['user_domain'])
        del(ctx_dict['user_identity'])
        del(ctx_dict['resource_uuid'])
        del(ctx_dict['project_domain'])
        del(ctx_dict['tenant'])
        self.assertEqual(self.ctx, ctx_dict)
