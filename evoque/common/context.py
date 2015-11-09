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

from oslo_context import context


class RequestContext(context.RequestContext):
    """Extends security contexts from the OpenStack common library."""

    def __init__(self, auth_token=None, auth_url=None, domain_id=None,
                 domain_name=None, user_name=None, user_id=None,
                 project_name=None, project_id=None, roles=None,
                 is_admin=False, read_only=False, show_deleted=False,
                 request_id=None, trust_id=None, auth_token_info=None,
                 all_tenants=False, **kwargs):
        """Stores several additional request parameters:

        :param domain_id: The ID of the domain.
        :param domain_name: The name of the domain.

        """
        self.user_name = user_name
        self.user_id = user_id
        self.project_name = project_name
        self.project_id = project_id
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.roles = roles
        self.auth_url = auth_url
        self.auth_token_info = auth_token_info
        self.trust_id = trust_id
        self.all_tenants = all_tenants

        super(RequestContext, self).__init__(auth_token=auth_token,
                                             user=user_name,
                                             tenant=project_name,
                                             is_admin=is_admin,
                                             read_only=read_only,
                                             show_deleted=show_deleted,
                                             request_id=request_id)

    def to_dict(self):
        value = super(RequestContext, self).to_dict()
        value.update({'auth_token': self.auth_token,
                      'auth_url': self.auth_url,
                      'domain_id': self.domain_id,
                      'domain_name': self.domain_name,
                      'user_name': self.user_name,
                      'user_id': self.user_id,
                      'project_name': self.project_name,
                      'project_id': self.project_id,
                      'is_admin': self.is_admin,
                      'read_only': self.read_only,
                      'roles': self.roles,
                      'show_deleted': self.show_deleted,
                      'request_id': self.request_id,
                      'trust_id': self.trust_id,
                      'auth_token_info': self.auth_token_info,
                      'all_tenants': self.all_tenants})
        return value

    @classmethod
    def from_dict(cls, values):
        return cls(**values)


def make_context(*args, **kwargs):
    return RequestContext(*args, **kwargs)
