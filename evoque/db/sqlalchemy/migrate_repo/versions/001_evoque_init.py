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

import sqlalchemy

from evoque.db.sqlalchemy import types


def upgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    ticket = sqlalchemy.Table(
        'ticket', meta,
        sqlalchemy.Column('id', sqlalchemy.String(36),
                          primary_key=True, nullable=False),
        sqlalchemy.Column('name', sqlalchemy.String(255)),
        sqlalchemy.Column('type', sqlalchemy.String(255)),
        sqlalchemy.Column('status', sqlalchemy.String(255)),
        sqlalchemy.Column('meta_data', types.Dict),
        sqlalchemy.Column('user', sqlalchemy.String(32), nullable=False),
        sqlalchemy.Column('project', sqlalchemy.String(32), nullable=False),
        sqlalchemy.Column('domain', sqlalchemy.String(32)),
        sqlalchemy.Column('user_id', sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column('project_id', sqlalchemy.String(255),
                          nullable=False),
        sqlalchemy.Column('domain_id', sqlalchemy.String(255)),
        sqlalchemy.Column('created_time', sqlalchemy.DateTime),
        sqlalchemy.Column('updated_time', sqlalchemy.DateTime),
        sqlalchemy.Column('deleted_time', sqlalchemy.DateTime),
        mysql_engine='InnoDB',
        mysql_charset='utf8'
    )

    tables = (
        ticket,
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
