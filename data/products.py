import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Products(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    instrument_type = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("instrument_types.id"))
