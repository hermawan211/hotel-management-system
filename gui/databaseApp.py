from tkinter import *
import tkinter as tk
import sqlite3

from datetime import date

today = date.today()
today = today.strftime("%d-%m-%y")

class DatabaseIntraction():
    def __init__(self):

        # Create or connect to a database
        self.conn = sqlite3.connect('guest_record.db')

        # database cursor
        self.c = self.conn.cursor()

        # create table
        self.c.execute('''CREATE TABLE IF NOT EXISTS guests (
                    name text,
                    phone text,
                    check_in text,
                    check_out text,
                    room text, 
                    room_condition text
                    )''')

    def write_data(self, name, phone, dateIn, dateOut, room, room_condition):

        # Insert Into table
        self.c.execute("INSERT INTO guests VALUES (:name, :phone, :dateIn, :dateOut, :room, :room_condition)",
                (name, phone, dateIn, dateOut, room, room_condition)
                )
        
        # Commit changes
        self.conn.commit()

    def display_records(self):

        self.c.execute("SELECT oid, * FROM guests")
        records = self.c.fetchall()
        print_records = '\n'.join(str(record) for record in records)
        #self.conn.close()
        return print_records
    
    def display_active_room(self):
        self.c.execute("SELECT * FROM guests WHERE check_out >= ?", (today,))
        records = self.c.fetchall()
        print_records = '\n'.join(str(record) for record in records)
        return print_records

    def delete_data(self, destination):
        # delete
        self.c.execute("DELETE from guests WHERE oid=" + destination)

        self.conn.commit()

    # room condition
    def get_room_status(self, room):

        self.c.execute("SELECT * FROM guests WHERE check_out == ?", (today,))
        to_be_cleaned = self.c.fetchall()

        self.c.execute("SELECT * FROM guests WHERE check_out > ?", (today,))
        occupied = self.c.fetchall()

        room_to_be_cleaned = [record[4] for record in to_be_cleaned]
        room_occupied = [record[4] for record in occupied]

        if room in room_to_be_cleaned:
            return 'Idle'
        elif room in room_occupied:
            return 'Full'
        else:
            return 'Empty'