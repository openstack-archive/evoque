# Copyright (c) 2012 NTT DOCOMO, INC.
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

"""Evoque DB test base class."""

import fixtures
from oslo_config import cfg

from evoque.db import api as db_api
from evoque.tests.unit import base

CONF = cfg.CONF

_DB_CACHE = None


class Database(fixtures.Fixture):

    def __init__(self, db_api):
        self.engine = db_api.get_engine()

    def _setUp(self):
        db_api.db_sync(self.engine)
        self.engine.connect()


class DBTestCase(base.TestCase):

    def setUp(self):
        super(DBTestCase, self).setUp()

        self.db_api = db_api

        global _DB_CACHE
        if not _DB_CACHE:
            _DB_CACHE = Database(db_api)
        self.useFixture(_DB_CACHE)
