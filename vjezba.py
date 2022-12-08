import tkinter as tk
from tkinter import ttk
from utils.util import create_label, create_smaller_label, get_image, get_foreground, create_frame, forgot_password, add_plant
import customtkinter
import sqlite3


conn = sqlite3.connect("PyFlora.db")
c = conn.cursor()


def create_sensor_table():
    try:
        c.execute(
            'CREATE TABLE IF NOT EXISTS  RecordsOfPlants (Plant_id INTEGER PRIMARY KEY, Plant TEXT, Photo BLOB)')
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


create_sensor_table()
insert_plant_data()
add_plant()
