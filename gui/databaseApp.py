from tkinter import *
import tkinter as tk
import sqlite3

# Create or connect to a database
conn = sqlite3.connect('guest_record.db')

# database cursor
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS guests (
            name text,
            phone text,
            check_in text,
            check_out text,
            room text, 
            room_condition text
            )''')

def write_data(name, phone, dateIn, dateOut, room, room_condition):
    
    conn = sqlite3.connect('guest_record.db')
    c = conn.cursor()

    # Insert Into table
    c.execute("INSERT INTO guests VALUES (:name, :phone, :dateIn, :dateOut, :room, :room_condition)",
              (name, phone, dateIn, dateOut, room, room_condition)
              )
    
    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()
