from tkinter import Toplevel
from PIL import Image
import datetime as dt


def get_hum():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Humidity")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}%\t\t {row[2]}"


def get_optimal_hum():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Humidity WHERE Value = 40")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}%\t\t {fetch[2]}"


def get_temp():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Temperature")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}°C\t {row[2]}"


def get_optimal_temp():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Temperature WHERE Value = 22")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}°C\t {fetch[2]}"


def get_bright():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Brightness")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}\t\t {row[2]}"


def get_optimal_bright():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value, Action FROM Brightness WHERE Value = 7")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}\t\t {fetch[2]}"


def get_ph():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value FROM pH")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}"


def get_optmal_ph():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value FROM pH Where Value = 7")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}"


def get_sal():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value FROM Salinity")
    fetch = c.fetchall()
    conn.close()
    for row in fetch:
        return f"{row[0]}  {row[1]}"


def get_optimal_sal():
    import sqlite3
    conn = sqlite3.connect('Sensors.db')
    c = conn.cursor()

    c.execute("SELECT Lines, Value FROM Salinity WHERE Value = 7")
    fetch = c.fetchone()
    conn.close()
    return f"{fetch[0]}  {fetch[1]}"
