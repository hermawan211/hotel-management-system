import tkinter as tk
from tkinter import ttk

class GuestView(tk.Frame):
    def __init__(self, parent, controlller):
        super().__init__(parent)

        label = ttk.Label(self, text="Guests")
        label.pack(pady=20, padx=20)

        