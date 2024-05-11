import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from gui.bookingUI import *
from gui.databaseApp import *

class DashboardView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.style = Style()
        self.style.configure('room.TButton', background='#CDCDCD', foreground="#E5A535")

        # Create parent frame for layout
        self.dashboard_frame = ttk.Frame(self)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

        # ------------------ Premium Frame ------------------

        self.premium_frame = ttk.Frame(self.dashboard_frame)
        self.premium_frame.grid(row=0, column=0, sticky="s",)

        self.list_premium_room = ['A-01', 'A-101', 'A-102', 'A-103', 'A-104',
                             'A-201', 'A-202', 'A-203', 'A-204']

        self.generate_premium_container(self.list_premium_room, self.premium_frame)
        
        # ------------------ Standart Frame ------------------
        self.standart_frame = ttk.Frame(self.dashboard_frame)
        self.standart_frame.grid(row=1, column=0, sticky="nsew", padx=30)
      

        self.list_standart_room = ['B-01', 'B-02','B-101', 'B-102', 'B-103', 'B-104',
                             'B-201', 'B-202', 'B-203', 'B-204', 'B-301', 'B-302',
                             'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                             'B-309', 'B-310', 'B-311']

        self.generate_standard_container(self.list_standart_room, self.standart_frame)

    def generate_premium_container(self, list_room, frame):

        premium_label = ttk.Label(self.premium_frame, text="Premium Room",
                                  font=("Helvetica", 14, "bold"))
        premium_label.grid(row=0, column=0, columnspan=5)

        for i, room in enumerate(list_room):
            premium_container = self.create_container(room, frame)

            if i < 5:
                premium_container.grid(row=1, column=i, padx=2, pady=2)
            else:
                premium_container.grid(row=2, column=i-5, padx=2, pady=2, columnspan=2)
            

    def generate_standard_container(self, list_room, frame):

        standart_label = ttk.Label(self.standart_frame, text="Standart Room",
                                  font=("Helvetica", 14, "bold"))
        standart_label.grid(row=0, column=0, columnspan=7)

        for i, room in enumerate(list_room):
            standart_container = self.create_container(room, frame)

            if i < 7:
                standart_container.grid(row=1, column=i, padx=2, pady=2)
            elif i < 14:
                standart_container.grid(row=2, column=i-7, padx=2, pady=2)
            else:
                standart_container.grid(row=3, column=i-14, padx=2, pady=2)

    def create_container(self, list_room, frame):
        
        self.db_interaction = DatabaseIntraction()
        current_room_status = self.db_interaction.get_room_status(list_room)

        container = ttk.Frame(frame, style="Container.TFrame", borderwidth=1, relief="raised")
        container.grid()

        self.style = Style()
        self.style.configure("Container.TFrame", background='#CDCDCD')

        # Photo
        roomPhoto = tk.PhotoImage(file='images/room.png')
        roomPhoto = roomPhoto.subsample(1, 1)

        roomPhoto_label = ttk.Label(container, image=roomPhoto, background='#CDCDCD')
        roomPhoto_label.image = roomPhoto
        roomPhoto_label.grid(row=0, column=0, rowspan=3, sticky='nswe', padx=5, pady=5)

        # Room indicator

        room_condition = ttk.Label(container, text=current_room_status, font=("Helvetica", 10, "bold")
                               , background='#CDCDCD')
        room_condition.grid(row=0, column=1, padx=(18,0), columnspan=2)

        room_led = tk.PhotoImage(file=f'images/{current_room_status}.png')
        room_led_label = ttk.Label(container, image=room_led, background='#CDCDCD')
        room_led_label.image = room_led
        room_led_label.grid(row=0, column=1, sticky='w', )

        # Room Number
        room_label = ttk.Label(container, text=list_room, font=("Helvetica", 10, "bold")
                               , background='#CDCDCD')
        room_label.grid(row=1, column=1, columnspan=2)

        # Room Button
        if current_room_status == 'Empty':
            room_btn = ttk.Button(container, text="Book", command=lambda room=list_room: self.open_booking(room),
                                  style='room.TButton',)
            room_btn.grid(row=2, column=1)
            

        elif current_room_status == 'Idle':
            room_btn = ttk.Button(container, text="Add", command=lambda room=list_room: self.add_booking(room), width=5,
                                  style='room.TButton',)
            room_btn.grid(row=2, column=1, sticky='w',)
            room_btn = ttk.Button(container, text="Clean", command=lambda room=list_room: self.clean_booking(room), width=4.99,
                                  style='room.TButton',)
            room_btn.grid(row=2, column=2, sticky='e',)

        elif current_room_status == 'Full':
            room_btn = ttk.Button(container, text="Add", command=lambda room=list_room: self.add_booking(room),
                                  style='room.TButton',)
            room_btn.grid(row=2, column=1)

        return container
    
    def refresher(self):
        # Destroy old premium containers
        for widget in self.premium_frame.winfo_children():
            widget.destroy()
        
        # new refreshed containers
        self.generate_premium_container(self.list_premium_room, self.premium_frame)

        # Destroy old standard containers
        for widget in self.standart_frame.winfo_children():
            widget.destroy()

        # new refreshed containers
        self.generate_standard_container(self.list_standart_room, self.standart_frame)
    
    def open_booking(self, room):
        
        def callback(booking_result):
            print(booking_result)
            if  booking_result=='Booked':
                self.refresher()
            else:
                print('Nope')

        booking = BookingView(self, room, self.controller, callback)

    def clean_booking(self, room):
        pass

    def add_booking(self, room):
        pass