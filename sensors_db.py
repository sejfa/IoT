import sqlite3
import datetime as dt
from random import randrange

conn = sqlite3.connect('Sensors.db')
c = conn.cursor()


def create_sensor_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS  Humidity (Date TEXT, Lines TEXT, Value INTEGER, Action TEXT)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS  Temperature (Date TEXT, Lines TEXT, Value INTEGER, Action TEXT)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS  pH (Date TEXT, Lines TEXT, Value INTEGER)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS  Brightness (Date TEXT, Lines TEXT, Value INTEGER, Action TEXT)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS  Salinity (Date TEXT, Lines TEXT, Value INTEGER)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS UserData (Name TEXT, Surname TEXT, Username TEXT, Password TEXT, Date TEXT)')


def insert_humidity_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current soil humidity is"

    action = ""

    for value in range(20, 61):
        if value < 40:
            action = "You need to water the plants"
        else:
            action = "No action needed"

        c.execute("INSERT INTO Humidity (Date, Lines, Value, Action) VALUES(?,?,?,?)",
                  (date, lines, value, action))
    conn.commit()


def insert_temperature_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current room temperature is"

    action = ""

    for value in range(22, 27):
        if value > 22:
            action = "Lower the room temperature"

        else:
            action = "No action needed"

        c.execute("INSERT INTO Temperature (Date, Lines, Value, Action) VALUES (?,?,?,?)",
                  (date, lines, value, action))
    conn.commit()


def insert_ph_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current pH is"
    value = randrange(6, 9)

    c.execute("INSERT INTO pH (Date, Lines, Value) VALUES (?,?,?)",
              (date, lines, value))
    conn.commit()


def insert_brightness_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current brightness is"

    action = ""

    for value in range(1, 11):
        if value <= 5:
            action = "Increase the brightness"
        else:
            action = "No action needed"

        c.execute("INSERT INTO Brightness (Date, Lines, Value, Action) VALUES (?,?,?,?)",
                  (date, lines, value, action))
    conn.commit()


def insert_salinity_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current salinity is"
    value = randrange(6, 13)

    c.execute("INSERT INTO Salinity (Date, Lines, Value) VALUES (?,?,?)",
              (date, lines, value))
    conn.commit()


create_sensor_table()


insert_humidity_data()


insert_temperature_data()


insert_brightness_data()

for i in range(20):
    insert_ph_data()

for i in range(20):
    insert_salinity_data()

c.close()
conn.close()
