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

        label = ttk.Label(self.guest_frame, text="Guests", font=("Helvetica", 18, 'bold'))
        label.grid(row=0, column=0,padx=(260,0), pady=(10, 20))

        # ------------------ Table frame ------------------
        self.guest_table = ttk.Frame(self.guest_frame,)
        self.guest_table.grid(row=1, column=0, sticky="nsew", padx=(180,0),)

        # Create table headers
        self.header_frame = ttk.Frame(self.guest_table)
        self.header_frame.grid()

        self.headers = ["Name", "Phone Number", "Check In", "Check Out", "Room"]
        self.column_widths = [40, 30, 20, 20, 5]
        self.header_labels = [] # store header labels for later reference
        self.header_widths = [15, 21, 5, 5, 5]
        for i, header in enumerate(self.headers):
            header_label = ttk.Label(self.header_frame, text= header, font=("Helvetica", 16, 'bold'))
            header_label.grid(row=0, column=i, padx=(0, self.header_widths[i]), pady=5, sticky='ns')
            self.header_labels.append(header_label)

        # scroll bar
        vScrollBar = ttk.Scrollbar(self.guest_frame, orient=VERTICAL)
        vScrollBar.grid(row=1, column=1, sticky="ns")

        # Create canvas to hold the data container
        canvas = tk.Canvas(self.guest_table, yscrollcommand=vScrollBar.set)
        canvas.grid(row=1, column=0, sticky="nsew")

        # link scroll bar to the container
        vScrollBar.config(command=canvas.yview)
        
        self.guest_container = ttk.Frame(canvas)
        canvas.create_window((0,0), window=self.guest_container, anchor=NW)

        # Configure canvas scrolling region
        self.guest_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # display records
        self.display_guests()

    def display_guests(self):
        # destroy widget for refresh
        for widget in self.guest_container.winfo_children():
            widget.destroy()

        # Obtaining records from database
        records = self.db_interaction.display_active_room().split('\n')

        # Filter out empty records
        records = [record for record in records if record.strip()]

        # Process non-empty records
        for i, record in enumerate(records):
            record_data = eval(record)
            for j, value in enumerate(record_data):
                data_label = ttk.Label(self.guest_container, text=value, font=("Helvetica", 11), anchor='center')
                data_label.grid(row=i + 2, column=j, padx=(0,0), pady=5, sticky='nw')

                # Adjust column width dynamically based on content length
                content_length = len(str(value))
                if content_length > self.column_widths[j]:
                    self.column_widths[j] = content_length

        # adjust the value dynamically
        for j, width in enumerate(self.column_widths):
            self.guest_container.grid_columnconfigure(j, minsize=width + 150) # can be adjusted

        for i, header_label in enumerate(self.header_labels):
            header_label.grid_configure(padx=(0, self.column_widths[i] + 40), pady=5)
