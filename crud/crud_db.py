import sqlite3
import tkinter as tk
import random



def get_plants():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()
    c.execute("SELECT Plant FROM RecordsOfPlants")
    result = c.fetchall()
    new_list = [item for i in result for item in i]
    
    return new_list

def get_plant_by_name(plantName):
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()
    c.execute("SELECT * FROM RecordsOfPlants WHERE Plant = ?", (plantName,))
    fetch = c.fetchone()

    plant = ({fetch[1]}, {fetch[2]}, {fetch[3]}, {fetch[4]}, {fetch[5]})      

    return plant 


def get_pots():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()
    c.execute("SELECT Pot, Plant FROM RecordsOfPots")
    result = c.fetchall()
    
    pot_list=[]

    for pot,plant in result:
        par = (pot, plant)
        pot_list.append(par)
    
    return pot_list


def get_pot_only():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()
    c.execute("SELECT Pot FROM RecordsOfPots")
    result = c.fetchall()
    new_list = [item for i in result for item in i]
    
    return new_list         



# Fetching sensors data
def convertTuple(tup):
    str = ''.join(tup)
    return str


def get_basil():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Humidity, Substrate, Place FROM RecordsOfPlants WHERE Plant ='Basil'")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]} {fetch[1]} {fetch[2]}"
    return result


def get_hosta():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Humidity, Substrate, Place FROM RecordsOfPlants WHERE Plant ='Hosta'")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]} {fetch[1]} {fetch[2]}"
    return result

def get_lilie():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Humidity, Substrate, Place FROM RecordsOfPlants WHERE Plant ='Lilies'")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]} {fetch[1]} {fetch[2]}"
    return result

def get_rose():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Humidity, Substrate, Place FROM RecordsOfPlants WHERE Plant ='Rose'")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]} {fetch[1]} {fetch[2]}"
    return result
################################################### Sensor details #####################################################

class Senzor:
    def __init__(self, vrijednost): #konstruktor - inicijalizira atribute objekta; konstruira objekt
        self.v = vrijednost         #v je atribut objekta Senzor

#napravi objekt tipa Senzor
senzor = Senzor(5)


senzor2 = Senzor(13)


def sensor_hum():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Unit, Action FROM Humidity ORDER BY RANDOM() LIMIT 1")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]}  {fetch[1]} {fetch[2]} {fetch[3]}"

    return result
    


def sensor_temp():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Unit, Action FROM Temperature ORDER BY RANDOM() LIMIT 1")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]}  {fetch[1]} {fetch[2]} {fetch[3]}"
    return result




def sensor_bright():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Brightness ORDER BY RANDOM() LIMIT 1")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}   {row[2]}"



def sensor_ph():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Ph ORDER BY RANDOM() LIMIT 1")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}  {row[2]}"




def sensor_sal():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Unit, Action FROM Salinity ORDER BY RANDOM() LIMIT 1")
    fetch = c.fetchone()
    conn.close()
    result = f"{fetch[0]}  {fetch[1]} {fetch[2]}  {fetch[3]}"
    return result


################################################### Plant details #####################################################

def plant_hum():
    
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Action FROM Humidity")
    fetch = c.fetchone()
    conn.close()
    convert = convertTuple(fetch)

    
    return convert



def plant_temp():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Action FROM Temperature")
    fetch = c.fetchone()
    conn.close()
    convert = convertTuple(fetch)
    return convert



def plant_bright():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Action FROM Brightness")
    fetch = c.fetchone()
    conn.close()
    convert = convertTuple(fetch)
    return convert



def plant_ph():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Action FROM pH")
    fetch = c.fetchone()
    conn.close()
    convert = convertTuple(fetch)
    return convert



def plant_sal():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Action FROM Salinity")
    fetch = c.fetchone()
    conn.close()
    convert = convertTuple(fetch)
    return convert



def get_optimal_hum():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Humidity WHERE Value = 40")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}%\t\t {fetch[2]}"




def get_temp():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Temperature")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}°C\t {row[2]}"




def get_optimal_temp():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Temperature WHERE Value = 22")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}°C\t {fetch[2]}"



def get_bright():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Brightness")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}\t\t\t {row[2]}"




def get_optimal_bright():

    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Brightness WHERE Value = 7")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}\t\t\t {fetch[2]}"




def get_ph():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM pH")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}\t\t {row[2]}"




def get_optmal_ph():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value FROM pH Where Value = 7")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}"




def get_sal():
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Salinity")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}\t\t {row[2]}"




def get_optimal_sal():
    
    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value FROM Salinity WHERE Value = 7")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}"

