import random
from baza_podataka.database import Humidity, Ph, Salinity, Temperature, Brightness
from baza_podataka.main import session


def get_humidity(session):
    return session.query(Humidity).all()


def get_random_humidity(session):
    humidity = get_humidity(session)

    random_humidity = random.choice(humidity)
    return random_humidity


def get_ph(session):
    return session.query(Ph).all()


def get_random_ph(session):
    ph = get_ph(session)

    random_ph = random.choice(ph)
    return random_ph


def get_salinity(session):
    return session.query(Salinity).all()


def get_random_salinity(session):
    salinity = get_ph(session)

    random_salinity = random.choice(salinity)
    return random_salinity


def get_temp(session):
    return session.query(Temperature).all()


def get_random_temp(session):
    temp = get_temp(session)

    random_temp = random.choice(temp)
    return random_temp


def get_brightness(session):
    return session.query(Brightness).all()


def get_random_brightness(session):
    brightness = get_brightness(session)

    random_brightness = random.choice(brightness)
    return random_brightness


def get_all_sensors(session):
    a = [get_random_temp(session),
         get_random_ph(session),
         get_random_salinity(session),
         get_random_brightness(session)]

    return random.choice(a)
