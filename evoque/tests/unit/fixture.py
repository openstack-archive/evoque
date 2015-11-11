# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
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

import fixtures
import sqlalchemy

from oslo_config import cfg

from evoque.db import api as db_api

CONF = cfg.CONF


class DBTestFixture(fixtures.Fixture):

    def __init__(self):
        # Use sqlite as test DB
        self.sqlite_db = '/tmp/evoque.db'

        CONF.set_default('connection', "sqlite://", group='database')
        CONF.set_default('sqlite_db', self.sqlite_db, group='database')
        CONF.set_default('sqlite_synchronous', False, group='database')

    def _setUp(self):
        self._setup_test_db()
        self.addCleanup(self._reset_test_db)

    def _setup_test_db(self):
        engine = db_api.get_engine()
        db_api.db_sync(engine)
        engine.connect()

    def _reset_test_db(self):
        engine = db_api.get_engine()
        meta = sqlalchemy.MetaData()
        meta.reflect(bind=engine)

        for table in reversed(meta.sorted_tables):
            if table.name == 'migrate_version':
                continue
            engine.execute(table.delete())
