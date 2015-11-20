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

'''
Interface for database access.

SQLAlchemy is currently the only supported backend.
'''

from oslo_config import cfg
from oslo_db import api

CONF = cfg.CONF

_BACKEND_MAPPING = {'sqlalchemy': 'evoque.db.sqlalchemy.api'}

IMPL = api.DBAPI.from_config(CONF, backend_mapping=_BACKEND_MAPPING)


def get_engine():
    return IMPL.get_engine()


def get_session():
    return IMPL.get_session()


# Tickets
def ticket_create(context, values):
    return IMPL.ticket_create(context, values)


def ticket_get_all(context, filters=None, limit=None, marker=None,
                   sort_key=None, sort_dir=None):
    return IMPL.ticket_get_all(context, filters=None, limit=None, marker=None,
                               sort_key=None, sort_dir=None)


# Workflows
def workflow_create(context, values):
    return IMPL.workflow_create(context, values)


def workflow_get_all(context, filters=None, limit=None, marker=None,
                     sort_key=None, sort_dir=None):
    return IMPL.workflow_get_all(context, filters=None, limit=None,
                                 marker=None, sort_key=None, sort_dir=None)


# Utils
def db_sync(engine, version=None):
    """Migrate the database to `version` or the most recent version."""
    return IMPL.db_sync(engine, version=version)


def db_version(engine):
    """Display the current database version."""
    return IMPL.db_version(engine)
