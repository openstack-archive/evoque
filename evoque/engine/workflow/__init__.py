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

import abc
import six

from oslo_config import cfg
from stevedore import driver

CONF = cfg.CONF


def get_workflow(engine=CONF.workflow_engine, namespace='evoque.workflow'):
    """Get workflow driver and load it.

    :param engine: workflow engine
    :param namespace: Namespace to use to look for drivers.
    """

    loaded_driver = driver.DriverManager(namespace, engine)
    return loaded_driver.driver()


@six.add_metaclass(abc.ABCMeta)
class Base(object):
    """Base class for workflow operations."""

    def __init__(self, wf_spec):
        super(Base, self).__init__()

    @abc.abstractmethod
    def workflow_create(self, wf_spec):
        """Create a workflow"""
