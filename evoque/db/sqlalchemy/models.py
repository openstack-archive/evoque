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

"""
SQLAlchemy models for Evoque data.
"""

import uuid

from oslo_db.sqlalchemy import models
import sqlalchemy
from sqlalchemy.ext import declarative

from evoque.db.sqlalchemy import types

BASE = declarative.declarative_base()


class EvoqueBase(models.TimestampMixin,
                 models.ModelBase):
    """Base class for Evoque Models."""

    __table_args__ = {'mysql_engine': 'InnoDB'}

    metadata = sqlalchemy.Column(types.Dict)

    user = sqlalchemy.Column(sqlalchemy.String(32))
    project = sqlalchemy.Column(sqlalchemy.String(32))
    domain = sqlalchemy.Column(sqlalchemy.String(32))
    user_id = sqlalchemy.Column(sqlalchemy.String(255))
    project_id = sqlalchemy.Column(sqlalchemy.String(255))
    domain_id = sqlalchemy.Column(sqlalchemy.String(255))


class Ticket(BASE, EvoqueBase):
    """Represents a ticket created by the Evoque engine."""

    __tablename__ = 'ticket'

    id = sqlalchemy.Column('id', sqlalchemy.String(36), primary_key=True,
                           default=lambda: str(uuid.uuid4()))
    workflow_id = sqlalchemy.Column(sqlalchemy.String(36),
                                    sqlalchemy.ForeignKey('workflow.id'))
    name = sqlalchemy.Column('name', sqlalchemy.String(255))
    type = sqlalchemy.Column(sqlalchemy.String(255))
    status = sqlalchemy.Column(sqlalchemy.String(255))


class Workflow(BASE, EvoqueBase):
    """Represents a workflow created by the Evoque engine."""

    __tablename__ = 'workflow'

    id = sqlalchemy.Column('id', sqlalchemy.String(36), primary_key=True,
                           default=lambda: str(uuid.uuid4()))
    name = sqlalchemy.Column('name', sqlalchemy.String(255))
    spec = sqlalchemy.Column('spec', types.MediumText())
