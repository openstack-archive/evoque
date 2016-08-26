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

from oslo_log import log as logging

from evoque.common.i18n import _
from evoque.common.i18n import _LE

LOG = logging.getLogger(__name__)


class NotImplementedError(NotImplementedError):
    pass


class EvoqueException(Exception):
    """Base Evoque Exception
    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.
    """
    message = _("An unknown exception occurred.")
    code = 500

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs and hasattr(self, 'code'):
            self.kwargs['code'] = self.code

        if message:
            self.message = message

        try:
            self.message = self.message % kwargs
        except Exception:
            # kwargs doesn't match a variable in the message
            # log the issue and the kwargs
            LOG.exception(_LE('Exception in string format operation, '
                              'kwargs: %s') % kwargs)
            raise

        super(EvoqueException, self).__init__(self.message)


class ConfigInvalid(EvoqueException):
    message = _("Invalid configuration file. %(error_msg)s")


class Invalid(EvoqueException):
    message = _("Unacceptable parameters.")
    code = 400


# Cannot be templated as the error syntax varies.
# msg needs to be constructed when raised.
class InvalidParameterValue(Invalid):
    message = _("%(err)s")
