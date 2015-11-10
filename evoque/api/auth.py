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

"""Access Control Lists (ACL's) control access the API server."""

from oslo_config import cfg

from evoque.api.middleware import auth_token


CONF = cfg.CONF


def install(app, conf, public_routes):
    """Install ACL check on application.
    :param app: A WSGI application.
    :param conf: Settings. Dict'ified and passed to keystone middleware
    :param public_routes: The list of the routes which will be allowed to
                          access without authentication.
    :return: The same WSGI application with ACL installed.
    """
    if not cfg.CONF.api.get('enable_authentication'):
        return app
    return auth_token.AuthTokenMiddleware(app,
                                          conf=dict(conf),
                                          public_api_routes=public_routes)
