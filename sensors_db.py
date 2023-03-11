import sqlite3
import datetime as dt


conn = sqlite3.connect("PyFlora.db")
c = conn.cursor()


def create_sensor_table():
    try:
        c.execute(
            'CREATE TABLE IF NOT EXISTS  RecordsOfPlants (Plant_id INTEGER PRIMARY KEY, Plant TEXT, Photo BLOB)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Humidity (Lines TEXT, Value INTEGER, Unit Text, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Temperature (Lines TEXT, Value INTEGER, Unit Text, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  pH (Lines TEXT, Value INTEGER, Unit Text, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Brightness (Lines TEXT, Value INTEGER, Action TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  Salinity (Lines TEXT, Value INTEGER, Unit Text, Action TEXT,  Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  UserData (Name TEXT, Surname TEXT, Username TEXT, Password TEXT, Date TEXT)')
        c.execute(
            'CREATE TABLE IF NOT EXISTS  RecordsOfPots (Pot_id INTEGER PRIMARY KEY, Pot TEXT, Plant TEXT)')
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
            print("Plant data is already inserted", error)

    insertdata(
        1, "Basil", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\Basil.jpg")
    insertdata(
        2, "Ginger", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\ginger.jpg")
    insertdata(
        3, "Hosta", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\hosta.jpg")
    insertdata(
        4, "Lilies", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lilie.jpg")
    insertdata(
        5, "Lavender","C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lavender.jpg")
    insertdata(
        6, "Lemon", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lemon.jpg")
    insertdata(
        7, "Mint", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\mint.jpg")
    insertdata(
        8, "Rose", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\Rose.jpg")
    insertdata(
        9, "Rosemary","C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\Rosemary.jpg")
    insertdata(
        10, "Origano","C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\oregano.jpg")

def insert_pot_data():
    def insert_data1(potid, pot, plant):
        
        try:
            insert_query = """ INSERT INTO RecordsOfPots
                                        (Pot_id, Pot, Plant) VALUES (?, ?, ?)"""
            data_tuple = (potid, pot, plant)
            c.execute(insert_query, data_tuple)

        except sqlite3.Error as error:
                print("Pot data is already inserted", error)
        
    insert_data1(1, "Kitchen - shelf by the window", "Basil")
    insert_data1(2, "Living room - small table near the couch","Hosta")
    insert_data1(3, "Balcony - near the window","Rose")
    insert_data1(4, "Bedroom - near the bed", "Lilies")
    

    
def insert_humidity_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current soil humidity is"
    unit = "%."
    action = ""

    for value in range(20, 61):
        if value < 30:
            action = "You need to water the plant daily!"
        elif value < 40:
            action = "You need to water the plant weekly."
        elif value < 50:
            action = "You need to water the plant monthly."
        else:
            action = "No action needed."

        c.execute("INSERT INTO Humidity (Lines, Value, Unit, Action, Date) VALUES(?,?,?,?,?)",
                  (lines, value, unit, action, date))
    conn.commit()


def insert_temperature_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current room temperature is"
    unit = "°C."
    action = ""

    for value in range(22, 27):
        if value > 22:
            action = "Lower the room temperature."

        else:
            action = "Soil temperature is optimal, no action needed."

        c.execute("INSERT INTO Temperature (Lines, Value, Unit, Action, Date) VALUES(?,?,?,?,?)",
                  (lines, value, unit, action, date))
    conn.commit()


def insert_ph_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current pH is"
    action = ""
    for value in range(6, 9):
        if value > 7:
            action = "Reduce soil pH."

        else:
            action = "Soil pH is fine, no action needed."

    c.execute("INSERT INTO pH (Lines, Value, Action, Date) VALUES (?,?,?,?)",
              (lines, value, action, date))
    conn.commit()


def insert_brightness_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current brightness is"

    action = ""

    for value in range(1, 11):
        if value <= 5:
            action = "The plant needs more light, move to a brighter place."
        else:
            action = "The plant has enough light, no action needed."

        c.execute("INSERT INTO Brightness (Lines, Value, Action, Date) VALUES (?,?,?,?)",
                  (lines, value, action, date))
    conn.commit()


def insert_salinity_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current salinity is"
    unit = "ppt."
    action = ""

    for value in range(1, 11):
        if value > 6:
            action = "Reduce soil salinity."
        else:
            action = "Soil salinity is fine, no action needed."
    c.execute("INSERT INTO Salinity (Lines, Value, Unit, Action, Date) VALUES (?,?,?,?,?)",
              (lines, value, unit, action, date))
    conn.commit()


create_sensor_table()
insert_plant_data()
insert_pot_data()
insert_humidity_data()
insert_temperature_data()
insert_brightness_data()


for i in range(20):
    insert_ph_data()

for i in range(20):
    insert_salinity_data()

c.close()
conn.close()
