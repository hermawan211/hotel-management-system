import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class BookingView(tk.Frame):
    def __init__(self, parent, room):
        super().__init__(parent)

        # Create parent frame for layout
        booking_frame = Toplevel()
        booking_frame.title("Booking")
        booking_frame.geometry("750x400")

        # Set the window position
        booking_frame.geometry("+{}+{}".format(270, 150))

        # ------------------ Booking Details ------------------
        booking_label = ttk.Label(booking_frame, text="Booking Details",
                                  font=("Helvetica", 14, "bold"))
        booking_label.grid(row=0, column=0, columnspan=3)

        name_label = ttk.Label(booking_frame, text="Name",
                                  font=("Helvetica", 12,))
        name_label.grid(row=1, column=0,)


        # room number
        room_label = ttk.Label(booking_frame, text=room,
                                  font=("Helvetica", 12,))
        room_label.grid(row=1, column=3,)
