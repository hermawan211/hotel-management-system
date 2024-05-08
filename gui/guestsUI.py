import tkinter as tk
from tkinter import ttk
import sqlite3

class GuestView(tk.Frame):
    def __init__(self, parent, controlller):
        super().__init__(parent)

        # Create parent frame for layout
        self.guest_frame = ttk.Frame(self)
        self.guest_frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(self.guest_frame, text="Guests")
        label.grid(row=0, column=0)

        conn = sqlite3.connect('guest_record.db')
        c = conn.cursor()

        # Create Query functions
        c.execute("SELECT *, oid FROM guests")
        records = c.fetchall()

        # getting all records
        print_records = ''
        for record in records:
            print_records += str(record[:-2]) + "\n"

        # label to fetch it on screen
        record_label = ttk.Label(self.guest_frame, text=print_records)
        record_label.grid(row=1, column=0)


        