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

        label = ttk.Label(self.data_frame, text="Data")
        label.grid(row=0, column=0)

        self.record_label = ttk.Label(self.data_frame, text="")
        self.record_label.grid(row=1, column=0, )

        self.delete_box = ttk.Entry(self.data_frame, width=50)
        self.delete_box.grid(row=2, column=0, pady=(30,0), sticky='w')

        # delete button
        delete_button = ttk.Button(self.data_frame, text="Delete", command=lambda: self.delete_data(self.delete_box.get()))
        delete_button.grid(row=2, column=0, pady=(30,0), sticky='e')

        # display records
        self.display_data()

    def display_data(self):
        self.record_label.config(text=self.db_interaction.display_records())

    def delete_data(self, rowNum):
        self.db_interaction.delete_data(rowNum)

        # Refresh displayed records after deletion
        self.display_data()
        self.controller.frames[GuestView.__name__].display_guests()
    