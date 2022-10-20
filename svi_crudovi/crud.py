import random
from baza_podataka.database import Humidity, Ph, Salinity, Temperature, Brightness
from baza_podataka.main import session
from PIL import Image


def get_background():
    background = '#F2F2F2'
    return background


def get_foreground():
    foreground = '#4D4D4D'
    return foreground


def get_label_font():
    font_style = 'Times New Roman', '15', 'bold italic'
    return font_style


def get_status_font():
    font_style = 'Times New Roman', '8', 'bold italic'
    return font_style


def get_image(image_name):
    root_folder_path = 'media'
    return Image.open(f"{root_folder_path}/{image_name}")


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
    a = get_random_temp(session)
    b = get_random_ph(session)
    c = get_random_salinity(session)
    d = get_random_brightness(session)
