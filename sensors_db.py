import sqlite3
import datetime as dt


conn = sqlite3.connect("PyFlora.db")
c = conn.cursor()


def create_sensor_table():
    try:
        c.execute(
            'CREATE TABLE IF NOT EXISTS  RecordsOfPlants (Plant_id INTEGER PRIMARY KEY, Plant TEXT, Photo BLOB, Humidity TEXT, Substrate TEXT, Place TEXT)')
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

def insert_user():
    def user(name,surname,username,password):

        try:
            date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
            insert_query = """ INSERT OR IGNORE INTO UserData (Name, Surname, Username, Password, Date) VALUES (?,?,?,?,?)"""
            data_tuple = (name, surname, username, password,date)
            c.execute(insert_query, data_tuple)

        except sqlite3.Error as error:
                print("User is already inserted", error)

    user("John","Wayne","johnwayne","helloworld")

def insert_plant_data():

    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            photo = file.read()
        return photo

    def insertdata(empId, name, photo, hum, sub, place):
        try:
            insert_query = """ INSERT or IGNORE INTO RecordsOfPlants
                                    (Plant_id, Plant, Photo, Humidity, Substrate, Place) VALUES (?,?,?,?,?,?)"""

            empPhoto = convertToBinaryData(photo)
            # Convert data into tuple format
            data_tuple = (empId, name, empPhoto, hum, sub, place)
            c.execute(insert_query, data_tuple)
            conn.commit()

        except sqlite3.Error as error:
            print("Plant data is already inserted", error)

    insertdata(
        1, "Basil", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\Basil.jpg","""Since the root of the plant is shallow, basil requires a relatively large amount of moisture. 
            During the growing season, it requires 600 to 650 mm2 of rainfall, and it especially needs moisture during the germination, sprouting, sprouting and budding stages.""","""The most recommended substrate for transplanted basil is substrate for outdoor plants or universal, mixed with normal soil. 
            As far as pH is concerned, this aromatic plant likes slightly more acidic, more precisely between 5.7 and 6.2.""","""It is not necessary to have a garden or an orchard to grow these plants, with jars and a place with a lot of light, ordinary light is enough.""")
    insertdata(
        2, "Hosta", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\hosta.jpg","""Hosta requires climatic conditions typical of open ground, i.e. it can grow in the apartment, but not for long, due to the lack of suitable conditions it will quickly wither. You can plant it in large pots and take it outside, or, in extreme cases, on the balcony.""",
            """In summer and spring, the plant needs to be fertilized with fertilizers, and already at the first planting, the hole needs to be fertilized with compost.""","""It has a highly developed root system, which does not allow excessive watering, it should be planted in places where the shade alternates with the sun.""")
    insertdata(
        3, "Lilies", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\lilie.jpg","""Lily (lat. Lilium) is an ornamental perennial known also under the names lilijan and lijer. It is assumed that it originates from Asia, more precisely from the area of ​​China, Japan and Korea. The lily prefers a moderate climate with moist soils and good drainage, with the fact that the soil should not be too wet. 
            The annual amount of precipitation that the plant needs depends on the type and place of planting, while the optimal amount ranges from 700 to 1,000 mm.""","""The lily prefers soil that is well-drained, moist, and rich in nutrients, and the best types of soil for growing lilies are deep, humus-rich, and permeable soils that retain moisture but don't stay too wet. 
            These soils are usually sandy and loamy soils with the addition of organic material such as compost, manure or leaf humus.""","""The lily thrives best in sunny or semi-shady places with a minimum of 6 hours of daily sunlight, and requires sufficient moisture and nutrients. Excessive sun can be harmful to lilies, especially if they are planted on the south side of a house or wall. Some lilies prefer lower growing areas while others can be found at significantly higher altitudes.""")
    insertdata(
        4, "Rose", "C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media\Rose.jpg","""Rose (lat. Rosa) is a herbaceous plant from the family of the same name (Rosaceae). It is one of 115 genera in the family, among which there are many edible species, when growing a young plant, care must be taken about watering. It has the greatest need for water in the summer, and it needs to be watered twice a week with stagnant water or rainwater. 
            It may be watered under the roots, and it is especially important to avoid watering the leaves during hot weather. For irrigation, it is best to use a drip system.""","""Manure or organic manure, nitrogen-based mineral fertilizers such as NPK or foliar fertilizers applied over the leaves can be used. In addition to this fertilizer, mineral or organic fertilizers are distributed in the ground 10 cm from the plant.""",
            """It is optimal to keep it in a semi-shady place protected from gusts of wind.""")
    

def insert_pot_data():
    def insert_data1(potid, pot, plant):
        
        try:
            insert_query = """ INSERT OR IGNORE INTO RecordsOfPots
                                        (Pot_id, Pot, Plant) VALUES (?,?,?)"""
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

    for value in range(20, 81 ):        
        if value < 30:
            action = "You need to water the plant daily!"
        elif value > 40 and value < 60:
            action = "You need to water the plant weekly."
        elif value > 60 and value < 80:
            action = "You need to water the plant monthly."
        else:
            action = "No action needed."

        c.execute("INSERT OR IGNORE INTO Humidity (Lines, Value, Unit, Action, Date) VALUES(?,?,?,?,?)",
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

        c.execute("INSERT OR IGNORE INTO Temperature (Lines, Value, Unit, Action, Date) VALUES(?,?,?,?,?)",
                  (lines, value, unit, action, date))
    conn.commit()


def insert_ph_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current pH is"
    action = ""
    for value in range(6, 9):
        if value > 8:
            action = "Reduce soil pH."

        else:
            action = "Soil pH is fine, no action needed."

    c.execute("INSERT OR IGNORE INTO pH (Lines, Value, Action, Date) VALUES (?,?,?,?)",
              (lines, value, action, date))
    conn.commit()


def insert_brightness_data():
    date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y")
    lines = "Current brightness is"

    action = ""

    for value in range(1, 10):
        if value <= 5:
            action = "The plant needs more light, move to a brighter place."
        else:
            action = "The plant has enough light, no action needed."

        c.execute("INSERT OR IGNORE INTO Brightness (Lines, Value, Action, Date) VALUES (?,?,?,?)",
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
    c.execute("INSERT OR IGNORE INTO Salinity (Lines, Value, Unit, Action, Date) VALUES (?,?,?,?,?)",
              (lines, value, unit, action, date))
    conn.commit()


create_sensor_table()
insert_user()
insert_plant_data()
insert_pot_data()
insert_humidity_data()
insert_temperature_data()
insert_brightness_data()


#for i in range(20):
insert_ph_data()

#for i in range(20):
insert_salinity_data()

c.close()
conn.close()
