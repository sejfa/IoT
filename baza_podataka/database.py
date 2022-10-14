import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Humidity(Base):
    __tablename__ = "vlažnost tla"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)

    def __str__(self):
        if self.range < 40:
            return f" Vlaznost tla je {self.range}%, treba zaliti biljku!"
        else:
            return f" Vlaznost tla je {self.range}%, ne treba zaliti biljku!"


class Ph(Base):
    __tablename__ = "pH vrijednost"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f"pH vrijednost je {self.range}."


class Salinity(Base):
    __tablename__ = "Salinitet tla"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f"salinitet zemlje je {self.range}."


class Temperature(Base):
    __tablename__ = "Temperatura prostorije"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f"temperature prostorije iznosi {self.range}."


class Brightness(Base):
    __tablename__ = "Razina svjetla koja dopire do prostorije"

    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Integer, nullable=False)

    def __str__(self):
        if self.range < 5:
            return f"Svjetlina iznosi {self.range}, pojačaj svjetlinu."

        else:
            return f"Svjetlina iznosi {self.range}."
