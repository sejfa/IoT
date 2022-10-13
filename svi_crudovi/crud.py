import random
from baza_podataka.database import Humidity, Ph, Salinity, Temperature


def get_humidity(session):
    return session.query(Humidity).all()


def get_random_humidity(session):
    humidity = get_humidity(session)

    random_humidity = random.choice(humidity)
    return random_humidity
