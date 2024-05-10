import tkinter as tk
from tkinter import ttk
import sqlite3

from gui.databaseApp import *

class GuestView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create parent frame for layout
        self.guest_frame = ttk.Frame(self)
        self.guest_frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(self.guest_frame, text="Guests")
        label.grid(row=0, column=0, sticky='n')

        self.record_label = ttk.Label(self.guest_frame, text="")
        self.record_label.grid(row=1, column=0, )

        self.db_interaction = DatabaseIntraction()

        # display records
        self.display_guests()

    def display_guests(self):
        records = self.db_interaction.display_active_room()
        self.record_label.config(text=records)
