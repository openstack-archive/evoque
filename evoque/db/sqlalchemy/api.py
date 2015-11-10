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
Implementation of SQLAlchemy backend.
'''

import sys

from oslo_config import cfg
from oslo_db import exception as db_exc
from oslo_db.sqlalchemy import session as db_session
from oslo_db.sqlalchemy import utils as db_utils

from evoque.common import exceptions
from evoque.common.i18n import _
from evoque.db.sqlalchemy import migration
from evoque.db.sqlalchemy import models

CONF = cfg.CONF

_facade = None


def get_facade():
    global _facade

    if not _facade:
        _facade = db_session.EngineFacade.from_config(CONF)
    return _facade

get_engine = lambda: get_facade().get_engine()
get_session = lambda: get_facade().get_session()


def get_backend():
    """The backend is this module itself."""
    return sys.modules[__name__]


def _session():
    return get_session()


def model_query(model, *args):
    session = _session()
    query = session.query(model, *args)
    return query


def _paginate_query(model, limit=None, marker=None, sort_key=None,
                    sort_dir=None, query=None):
    if not query:
        query = model_query(model)
    sort_keys = ['id']
    if sort_key and sort_key not in sort_keys:
        sort_keys.insert(0, sort_key)
    try:
        query = db_utils.paginate_query(query, model, limit, sort_keys,
                                        marker=marker, sort_dir=sort_dir)
    except db_exc.InvalidSortKey:
        raise exceptions.InvalidParameterValue(
            _('The sort_key value "%(key)s" is an invalid field for sorting')
            % {'key': sort_key})
    return query.all()


# Tickets
def ticket_create(context, values):
    ticket_ref = models.Ticket()
    ticket_ref.update(values)
    ticket_ref.save(_session())
    return ticket_ref


def ticket_get_all(context, filters=None, limit=None, marker=None,
                   sort_key=None, sort_dir=None):
    query = model_query(models.Ticket)
    return _paginate_query(models.Ticket, limit, marker,
                           sort_key, sort_dir, query)


# Utils
def db_sync(engine, version=None):
    """Migrate the database to `version` or the most recent version."""
    return migration.db_sync(engine, version=version)


def db_version(engine):
    """Display the current database version."""
    return migration.db_version(engine)
