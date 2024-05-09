from tkinter import *
import tkinter as tk
import sqlite3

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

    def delete_data(self, destination):
        # delete
        self.c.execute("DELETE from guests WHERE oid=" + destination)

        self.conn.commit()
