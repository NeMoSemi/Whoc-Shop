import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class InstrumentTypes(SqlAlchemyBase):
    __tablename__ = 'instrument_types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
