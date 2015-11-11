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

import six
from webob import exc

from heat.common.i18n import _
from heat.common import identifier


def policy_enforce(handler):
    """Decorator that enforces policies.

    Checks the path matches the request context and enforce policy defined in
    policy.json.

    This is a handler method decorator.
    """
    @six.wraps(handler)
    def handle_stack_method(controller, req, tenant_id, **kwargs):
        if req.context.tenant_id != tenant_id:
            raise exc.HTTPForbidden()
        allowed = req.context.policy.enforce(context=req.context,
                                             action=handler.__name__,
                                             scope=controller.REQUEST_SCOPE)
        if not allowed:
            raise exc.HTTPForbidden()
        return handler(controller, req, **kwargs)

    return handle_stack_method


def identified_stack(handler):
    """Decorator that passes a stack identifier instead of path components.

    This is a handler method decorator.
    """
    @policy_enforce
    @six.wraps(handler)
    def handle_stack_method(controller, req, stack_name, stack_id, **kwargs):
        stack_identity = identifier.HeatIdentifier(req.context.tenant_id,
                                                   stack_name,
                                                   stack_id)
        return handler(controller, req, dict(stack_identity), **kwargs)

    return handle_stack_method


def make_url(req, identity):
    """Return the URL for the supplied identity dictionary."""
    try:
        stack_identity = identifier.HeatIdentifier(**identity)
    except ValueError:
        err_reason = _('Invalid Stack address')
        raise exc.HTTPInternalServerError(err_reason)

    return req.relative_url(stack_identity.url_path(), True)


def make_link(req, identity, relationship='self'):
    """Return a link structure for the supplied identity dictionary."""
    return {'href': make_url(req, identity), 'rel': relationship}


def get_allowed_params(params, whitelist):
    """Extract from ``params`` all entries listed in ``whitelist``.

    The returning dict will contain an entry for a key if, and only if,
    there's an entry in ``whitelist`` for that key and at least one entry in
    ``params``. If ``params`` contains multiple entries for the same key, it
    will yield an array of values: ``{key: [v1, v2,...]}``

    :param params: a NestedMultiDict from webob.Request.params
    :param whitelist: an array of strings to whitelist

    :returns: a dict with {key: value} pairs
    """
    allowed_params = {}

    for key, get_type in six.iteritems(whitelist):
        value = None
        if get_type == 'single':
            value = params.get(key)
        elif get_type == 'multi':
            value = params.getall(key)
        elif get_type == 'mixed':
            value = params.getall(key)
            if isinstance(value, list) and len(value) == 1:
                value = value.pop()

        if value:
            allowed_params[key] = value

    return allowed_params
