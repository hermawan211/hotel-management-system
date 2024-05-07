import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from gui.bookingUI import *

class DashboardView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Create parent frame for layout
        self.dashboard_frame = ttk.Frame(self)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

        # ------------------ Premium Frame ------------------
        premium_frame = ttk.Frame(self.dashboard_frame)
        premium_frame.grid(row=0, column=0, sticky="s", pady=(0,30),)

        premium_label = ttk.Label(premium_frame, text="Premium Room",
                                  font=("Helvetica", 14, "bold"))
        premium_label.grid(row=0, column=0, columnspan=5)

        list_premium_room = ['A-01', 'A-101', 'A-102', 'A-103', 'A-104',
                             'A-201', 'A-202', 'A-203', 'A-204']

        self.generate_premium_container(list_premium_room, premium_frame)
        
        # ------------------ Standart Frame ------------------
        standart_frame = ttk.Frame(self.dashboard_frame)
        standart_frame.grid(row=1, column=0, sticky="nsew", padx=75)

        standart_label = ttk.Label(standart_frame, text="Standart Room",
                                  font=("Helvetica", 14, "bold"))
        standart_label.grid(row=0, column=0, columnspan=7)

        list_standart_room = ['B-01', 'B-02','B-101', 'B-102', 'B-103', 'B-104',
                             'B-201', 'B-202', 'B-203', 'B-204', 'B-301', 'B-302',
                             'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                             'B-309', 'B-310', 'B-311']

        self.generate_standard_container(list_standart_room, standart_frame)

    def generate_premium_container(self, list_room, frame):
        for i, room in enumerate(list_room):
            premium_container = self.create_container(room, frame)

            if i < 5:
                premium_container.grid(row=1, column=i, padx=2, pady=2)
            else:
                premium_container.grid(row=2, column=i-5, padx=2, pady=2, columnspan=2)
            

    def generate_standard_container(self, list_room, frame):
        for i, room in enumerate(list_room):
            standart_container = self.create_container(room, frame)

            if i < 7:
                standart_container.grid(row=1, column=i, padx=2, pady=2)
            elif i < 14:
                standart_container.grid(row=2, column=i-7, padx=2, pady=2)
            else:
                standart_container.grid(row=3, column=i-14, padx=2, pady=2)

    def create_container(self, list_room, frame):
        container = ttk.Frame(frame, style="Container.TFrame", borderwidth=1, relief="solid")
        container.grid()

        self.style = Style()
        self.style.configure("Container.TFrame", background='#CDCDCD')

        # Photo
        roomPhoto = tk.PhotoImage(file='images/room.png')
        roomPhoto = roomPhoto.subsample(1, 1)

        roomPhoto_label = ttk.Label(container, image=roomPhoto, background='#CDCDCD')
        roomPhoto_label.image = roomPhoto
        roomPhoto_label.grid(row=0, column=0, rowspan=3,)

        # Room indicator

        room_condition = ttk.Label(container, text="Empty", font=("Helvetica", 10, "bold")
                               , background='#CDCDCD')
        room_condition.grid(row=0, column=1, sticky='e')

        room_led = tk.PhotoImage(file='images/green.png')
        room_led_label = ttk.Label(container, image=room_led, background='#CDCDCD')
        room_led_label.image = room_led
        room_led_label.grid(row=0, column=1, sticky='w')

        # Room Number
        room_label = ttk.Label(container, text=list_room, font=("Helvetica", 10, "bold")
                               , background='#CDCDCD')
        room_label.grid(row=1, column=1)

        # Room Button
        room_btn = ttk.Button(container, text="Book", command=lambda room=list_room: self.open_booking(room))
        room_btn.grid(row=2, column=1)

        return container
    
    def open_booking(self, room):
        booking = BookingView(self, room)