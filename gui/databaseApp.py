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
        print_records = '\n'.join(str(record[:-1]) for record in records)
        #self.conn.close()
        return print_records
    
    def display_active_room(self):
        self.c.execute("SELECT * FROM guests WHERE check_out >= ? AND room_condition != 'Empty'", (today,))
        records = self.c.fetchall()
        print_records = '\n'.join(str(record[:-1]) for record in records)
        return print_records

    def delete_data(self, destination):
        # delete
        self.c.execute("DELETE from guests WHERE oid=" + destination)

        self.conn.commit()


    # room condition
    def get_room_status(self, room):

        self.c.execute("SELECT * FROM guests WHERE check_out == ? AND room_condition == 'Full'", (today,))
        to_be_cleaned = self.c.fetchall()

        self.c.execute("SELECT * FROM guests WHERE check_out > ? AND room_condition == 'Full'", (today,))
        occupied = self.c.fetchall()

        room_to_be_cleaned = [record[4] for record in to_be_cleaned]
        room_occupied = [record[4] for record in occupied]

        if room in room_to_be_cleaned:
            return 'Idle'
        elif room in room_occupied:
            return 'Full'
        else:
            return 'Empty'
        
    def get_guest_detail(self, room):
        self.c.execute("SELECT * FROM guests WHERE room = ? AND room_condition != 'Empty'", (room,))
        guest_detail = self.c.fetchall()

        return guest_detail

    def clean_room(self, room):
        self.c.execute("SELECT * FROM guests WHERE room = ? AND room_condition != 'Empty'", (room,))
        guest_detail = self.c.fetchall()
        print(guest_detail[0][1])

        self.c.execute("""UPDATE guests SET
                    name = :name,
                    phone = :phone,
                    check_in = :dateIn,
                    check_out = :dateOut,
                    room = :room, 
                    room_condition = "Empty"
                       
                    WHERE room = :room AND room_condition != 'Empty' """,
                    {
                        'name': guest_detail[0][0],
                        'phone': guest_detail[0][1],
                        'dateIn': guest_detail[0][2],
                        'dateOut': guest_detail[0][3],
                        'room': guest_detail[0][4]
                    })
        
        self.conn.commit()

    def edit_data(self, room, dateOut):
        self.c.execute("SELECT * FROM guests WHERE room = ? AND room_condition != 'Empty'", (room,))
        guest_detail = self.c.fetchall()
        print(guest_detail, dateOut)

        self.c.execute("""UPDATE guests SET
                    name = :name,
                    phone = :phone,
                    check_in = :dateIn,
                    check_out = :dateOut,
                    room = :room, 
                    room_condition = "Full"
                       
                    WHERE room = :room AND room_condition != 'Empty' """,
                    {
                        'name': guest_detail[0][0],
                        'phone': guest_detail[0][1],
                        'dateIn': guest_detail[0][2],
                        'dateOut': dateOut,
                        'room': guest_detail[0][4]
                    })
        
        self.conn.commit()
        
        for detail in guest_detail:
            pass