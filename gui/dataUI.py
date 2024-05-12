from tkinter import *
from tkinter import ttk
import tkinter as tk

from gui.databaseApp import *
from gui.guestsUI import *

class DataView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.db_interaction = DatabaseIntraction()

        # Create parent frame for layout
        self.data_frame = ttk.Frame(self)
        self.data_frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(self.data_frame, text="Data", font=("Helvetica", 16, 'bold'))
        label.grid(row=0, column=0,padx=(460,0), pady=(10, 20))

        # Create data frame for table
        self.data_table = ttk.Frame(self.data_frame, relief='ridge')
        self.data_table.grid(row=1, column=0, sticky="nsew", padx=(460,15))

        self.delete_box = ttk.Entry(self.data_frame, width=50)
        self.delete_box.grid(row=2, column=0, pady=(30,0), padx=(380, 0))

        # delete button
        delete_button = ttk.Button(self.data_frame, text="Delete", command=lambda: self.delete_data(self.delete_box.get()))
        delete_button.grid(row=2, column=0, pady=(30,0), sticky='e')

        # ------------------ Table frame ------------------

        # Create table headers
        # Create table headers
        self.header_frame = ttk.Frame(self.data_table)
        self.header_frame.grid()

        headers = ["No", "Name", "Phone", "Check In", "Check Out", "Room"]
        for i, header in enumerate(headers):
            header_label = ttk.Label(self.header_frame, text= header, font=("Helvetica", 12, 'bold'))
            header_label.grid(row=1, column=i, padx=5, pady=5)

        # scroll bar
        vScrollBar = ttk.Scrollbar(self.data_frame, orient=VERTICAL)
        vScrollBar.grid(row=1, column=1, sticky='ns',)

        # Create canvas to hold the data container
        canvas = tk.Canvas(self.data_table, yscrollcommand=vScrollBar.set)
        canvas.grid(row=1, column=0, sticky="nsew")

        # link scroll bar to the container
        vScrollBar.config(command=canvas.yview)
        
        self.data_container = ttk.Frame(canvas)
        canvas.create_window((0,0), window=self.data_container, anchor=NW)

        # Configure canvas scrolling region
        self.data_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # display records
        self.display_data()

    def display_data(self):

        # destroy widget for refresh
        for widget in self.data_container.winfo_children():
            widget.destroy()

        # Obtaining records from database
        records = self.db_interaction.display_records().split('\n')

        list_records = [eval(record) for record in records]
        
        for i, record in enumerate(list_records):
            for j, value in enumerate(record):
                data_label = ttk.Label(self.data_container, text=f"{value}  ", font=("Helvetica", 11))
                data_label.grid(row=i + 2, column=j, padx=(10,0), pady=5)

    def delete_data(self, rowNum):
        self.db_interaction.delete_data(rowNum)

        # Refresh displayed records after deletion
        self.display_data()
        self.controller.frames[GuestView.__name__].display_guests()
    