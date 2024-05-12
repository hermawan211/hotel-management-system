import tkinter as tk
from tkinter import ttk
import sqlite3

from gui.databaseApp import *

class GuestView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.db_interaction = DatabaseIntraction()

        # Create parent frame for layout
        self.guest_frame = ttk.Frame(self)
        self.guest_frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(self.guest_frame, text="Guests", font=("Helvetica", 16, 'bold'))
        label.grid(row=0, column=0,padx=(460,0), pady=(10, 20))

        # Create parent frame for layout
        self.guest_table = ttk.Frame(self.guest_frame, relief='ridge')
        self.guest_table.grid(row=1, column=0, sticky="nsew", padx=(460,0))

        # display records
        self.display_guests()

    def display_guests(self):

        # destroy widget for refresh
        for widget in self.guest_table.winfo_children():
            widget.destroy()

        # Create table headers
        headers = ["Name", "Phone", "Check In", "Check Out", "Room"]

        for i, header in enumerate(headers):
            header_label = ttk.Label(self.guest_table, text= header, font=("Helvetica", 12, 'bold'))
            header_label.grid(row=1, column=i, padx=5, pady=5)

        # Obtaining records from database
        records = self.db_interaction.display_active_room().split('\n')

        list_records = [eval(record) for record in records]
        
        for i, record in enumerate(list_records):
            for j, value in enumerate(record):
                data_label = ttk.Label(self.guest_table, text=value, font=("Helvetica", 10))
                data_label.grid(row=i + 2, column=j, padx=5, pady=5)
