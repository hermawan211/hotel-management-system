import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from datetime import date

today = date.today()
today = today.strftime("%d-%m-%Y")

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
        booking_label.grid(row=0, column=0, )

        # date
        date_label = ttk.Label(booking_frame, text=today,
                               font=("Helvetica", 12, ))
        date_label.grid(row=0, column=1, sticky='e', padx=(60, 0))

        # room number
        room_label = ttk.Label(booking_frame, text=room,
                                  font=("Helvetica", 12, 'bold'))
        room_label.grid(row=0, column=2,padx=(20, 0))

        # name
        name_label = ttk.Label(booking_frame, text="Name: ",
                                  font=("Helvetica", 12,))
        name_label.grid(row=1, column=0, pady=(40,0))

        self.name_entry = ttk.Entry(booking_frame, font=("Helvetica", 12))
        self.name_entry.grid(row=1, column=1, padx=(40,), pady=(40,0))

        # Phone
        phone_label = ttk.Label(booking_frame, text="Phone: ",
                                  font=("Helvetica", 12,))
        phone_label.grid(row=2, column=0,)

        self.phone_entry = ttk.Entry(booking_frame, font=("Helvetica", 12))
        self.phone_entry.grid(row=2, column=1, padx=(40,))

        # Checkout date entry
        checkout_label = ttk.Label(booking_frame, text="Checkout Date: ",
                                    font=("Helvetica", 12,))
        checkout_label.grid(row=3, column=0)

        # Cancel
        cancel_button = ttk.Button(booking_frame, text="Cancel", command=self.cancel_data)
        cancel_button.grid(row=5, column=0)

        # submit
        submit_button = ttk.Button(booking_frame, text="Submit", command=self.submit_data)
        submit_button.grid(row=5, column=1)

    def cancel_data(self):
        pass

    def submit_data(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        dateIn = today

        