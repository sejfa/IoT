import sqlite3
import random
import datetime as dt

conn = sqlite3.connect('Sensors.db')
c = conn.cursor()


class AllSensors():
    def __init__(self) -> None:
        super().__init__()

    def create_sensor_table():
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Humidity (Date TEXT, Lines TEXT, Value INTEGER, Action TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Temperature (Date TEXT, Lines TEXT, Value INTEGER)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  pH (Date TEXT, Lines TEXT, Value INTEGER)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Brightness (Date TEXT, Lines TEXT, Value INTEGER, Action TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Salinity (Date TEXT, Lines TEXT, Value INTEGER, Action TEXT)')

    def insert_humidity_data():
        date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
        lines = "Current soil humidity is"
        value = random.randrange(20, 61)
        action = ""

        if value < 40:
            action = "You need to water the plants"
        else:
            action = "No action needed"

        c.execute("INSERT INTO Humidity (Date, Lines, Value, Action) VALUES (?,?,?,?)",
                  (date, lines, value, action))
        conn.commit()

    def insert_temperature_data():
        date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
        lines = "Current room emperature is"
        value = random.randrange(22, 27)

        c.execute("INSERT INTO Humidity (Date, Lines, Value) VALUES (?,?,?,?)",
                  (date, lines, value))
        conn.commit()

    def insert_ph_data():
        date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
        lines = "Current pH is"
        value = random.randrange(6, 8)

        c.execute("INSERT INTO Humidity (Date, Lines, Value) VALUES (?,?,?,?)",
                  (date, lines, value))
        conn.commit()

    def insert_brightness_data():
        date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
        lines = "Current brightness is"
        value = random.randrange(1, 11)
        action = ""

        if value <= 4:
            action = "Increase the brightness"
        else:
            action = "No action needed"

        c.execute("INSERT INTO Humidity (Date, Lines, Value, Action) VALUES (?,?,?,?)",
                  (date, lines, value, action))
        conn.commit()

    def insert_salinity_data():
        date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
        lines = "Current salinity is"
        value = random.randrange(6, 8)

        c.execute("INSERT INTO Humidity (Date, Lines, Value) VALUES (?,?,?,?)",
                  (date, lines, value))
        conn.commit()

    create_sensor_table()

    for i in range(5):
        insert_humidity_data()

    for i in range(5):
        insert_temperature_data()

    for i in range(5):
        insert_ph_data()

    for i in range(5):
        insert_brightness_data()

    for i in range(5):
        insert_salinity_data()

    c.close()
    conn.close()
