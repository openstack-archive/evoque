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

"""Utilities and helper functions."""

import six

from oslo_log import log as logging

from evoque.common.i18n import _LW

LOG = logging.getLogger(__name__)


def safe_rstrip(value, chars=None):
    """Removes trailing characters from a string if that does not make it empty
    :param value: A string value that will be stripped.
    :param chars: Characters to remove.
    :return: Stripped value.
    """
    if not isinstance(value, six.string_types):
        LOG.warn(_LW("Failed to remove trailing character. Returning original "
                     "object. Supplied object is not a string: %s,"), value)
        return value

    return value.rstrip(chars) or value
