import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Humidity(Base):
    __tablename__ = "vlažnost tla"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)


class Ph(Base):
    __tablename__ = "pH vrijednost"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)


class Salinity(Base):
    __tablename__ = "Salinitet tla"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)


class Temperature(Base):
    __tablename__ = "Temperatura prostorije"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)
