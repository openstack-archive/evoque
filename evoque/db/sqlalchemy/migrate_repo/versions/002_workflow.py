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

from sqlalchemy import Column, Table, MetaData
from sqlalchemy import String, DateTime

from evoque.db.sqlalchemy import types


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    workflow = Table(
        'workflow', meta,
        Column('id', String(36),
               primary_key=True, nullable=False),
        Column('name', String(255)),
        Column('type', String(255)),
        Column('status', String(255)),
        Column('user', String(32)),
        Column('project', String(32)),
        Column('domain', String(32)),
        Column('user_id', String(255)),
        Column('project_id', String(255)),
        Column('domain_id', String(255)),
        Column('steps', String(255)),
        Column('metadata', types.Dict),
        Column('created_at', DateTime),
        Column('updated_at', DateTime),
        Column('deleted_at', DateTime),
        mysql_engine='InnoDB',
        mysql_charset='utf8'
    )

    tables = (
        workflow,
    )

    for index, table in enumerate(tables):
        try:
            table.create()
        except Exception:
            # If an error occurs, drop all tables created so far to return
            # to the previously existing state.
            meta.drop_all(tables=tables[:index])
            raise


def downgrade(migrate_engine):
    raise NotImplementedError('Database downgrade not supported - '
                              'would drop all tables')
