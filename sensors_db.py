import sqlite3
import datetime as dt
from random import randrange

conn = sqlite3.connect("PyFlora.db")
c = conn.cursor()


def create_sensor_table():
    try:
        c.execute(
            'CREATE TABLE IF NOT EXISTS  RecordsOfPlants (Plant_id INTEGER PRIMARY KEY, Plant TEXT, Photo BLOB)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Humidity (Lines TEXT, Value INTEGER, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Temperature (Lines TEXT, Value INTEGER, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  pH (Lines TEXT, Value INTEGER, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Brightness (Lines TEXT, Value INTEGER, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Salinity (Lines TEXT, Value INTEGER, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  UserData (Name TEXT, Surname TEXT, Username TEXT, Password TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Vessels (vessel_id INTEGER, Vessel TEXT)')
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error: '{e}'")

    return conn


def insert_plant_data():

    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            photo = file.read()
        return photo

    def insertdata(empId, name, photo):
        try:
            insert_query = """ INSERT INTO RecordsOfPlants
                                    (Plant_id, Plant, Photo) VALUES (?, ?, ?)"""

            empPhoto = convertToBinaryData(photo)

            # Convert data into tuple format
            data_tuple = (empId, name, empPhoto)
            c.execute(insert_query, data_tuple)
            conn.commit()

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)

    insertdata(
        1, "Basil", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\Basil.jpg")
    insertdata(
        2, "Ginger", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\ginger.jpg")
    insertdata(
        3, "Hosta", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\hosta.jpg")
    insertdata(
        4, "Lilies", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lilie.jpg")
    insertdata(5, "Lavender",
               "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lavender.jpg")
    insertdata(
        6, "Lemon", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lemon.jpg")
    insertdata(
        7, "Mint", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\mint.jpg")
    insertdata(
        8, "Rose", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\mint.jpg")
    insertdata(9, "Rosemary",
               "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\mint.jpg")
    insertdata(10, "Origano",
               "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\mint.jpg")


def insert_humidity_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current soil humidity is"

    action = ""

    for value in range(20, 61):
        if value < 30:
            action = "You need to water the plants daily"
        elif value < 40:
            action = "You need to water the plants weekly"
        elif value < 50:
            action = "You need to water the plants monthly"
        else:
            action = "No action needed"

        c.execute("INSERT INTO Humidity (Lines, Value, Action, Date) VALUES(?,?,?,?)",
                  (lines, value, action, date))
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

        c.execute("INSERT INTO Temperature (Lines, Value, Action, Date) VALUES(?,?,?,?)",
                  (lines, value, action, date))
    conn.commit()


def insert_ph_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current pH is"
    value = randrange(6, 9)

    c.execute("INSERT INTO pH (Lines, Value,  Date) VALUES (?,?,?)",
              (lines, value, date))
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

        c.execute("INSERT INTO Brightness (Lines, Value, Action, Date) VALUES (?,?,?,?)",
                  (lines, value, action, date))
    conn.commit()


def insert_salinity_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current salinity is"
    value = randrange(6, 13)

    c.execute("INSERT INTO Salinity (Lines, Value, Date) VALUES (?,?,?)",
              (lines, value, date))
    conn.commit()


create_sensor_table()
#insert_plant_data()
# insert_humidity_data()
# insert_temperature_data()
# insert_brightness_data()


# for i in range(20):
# insert_ph_data()

# for i in range(20):
# insert_salinity_data()

c.close()
conn.close()
