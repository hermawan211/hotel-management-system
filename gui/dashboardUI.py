import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from gui.bookingUI import *
from gui.databaseApp import *
from gui.guestsUI import *

class DashboardView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        
        self.style = Style()
        self.style.configure('room.TButton', background='#CDCDCD', foreground="#E5A535")

        # Create parent frame for layout
        self.dashboard_frame = ttk.Frame(self)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

        # ------------------ Deluxe Frame ------------------

        self.deluxe_frame = ttk.Frame(self.dashboard_frame)
        self.deluxe_frame.grid(row=0, column=0, sticky="w", padx=(80,0))

        self.list_deluxe_room = ['A-01', 'B-01', 'B-02',]

        self.generate_deluxe_container(self.list_deluxe_room, self.deluxe_frame)

        # ------------------ Superior I Frame ------------------

        self.superI_frame = ttk.Frame(self.dashboard_frame)
        self.superI_frame.grid(row=1, column=0, )

        self.list_superI_room = ['A-101', 'A-102', 'A-103', 'A-104',
                                 'B-101', 'B-102', 'B-103', 'B-104',]

        self.generate_superI_container(self.list_superI_room, self.superI_frame)

        # ------------------ Superior II Frame ------------------

        self.superII_frame = ttk.Frame(self.dashboard_frame)
        self.superII_frame.grid(row=2, column=0, sticky="s",)

        self.list_superII_room = ['A-201', 'A-202', 'A-203', 'A-204',
                                  'B-201', 'B-202', 'B-203', 'B-204',
                                  'B-301', 'B-302', 'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                                 ]

        self.generate_superII_container(self.list_superII_room, self.superII_frame)
        
        # ------------------ Standard Frame ------------------
        self.standard_frame = ttk.Frame(self.dashboard_frame)
        self.standard_frame.grid(row=0, column=0, sticky='e', padx=(0, 80))

        self.list_standard_room = ['B-309', 'B-310', 'B-311']

        self.generate_standard_container(self.list_standard_room, self.standard_frame)

    def generate_deluxe_container(self, list_room, frame):

        deluxe_label = ttk.Label(self.deluxe_frame, text="Deluxe",
                                  font=("Helvetica", 14, "bold"))
        deluxe_label.grid(row=0, column=0, columnspan=4)

        for i, room in enumerate(list_room):
            deluxe_container = self.create_container(room, frame)
            deluxe_container.grid(row=1, column=i, padx=2, pady=2)

    def generate_standard_container(self, list_room, frame):

        standard_label = ttk.Label(self.standard_frame, text="Standard",
                                  font=("Helvetica", 14, "bold"))
        standard_label.grid(row=0, column=0, columnspan=4)

        for i, room in enumerate(list_room):
            standard_container = self.create_container(room, frame)
            standard_container.grid(row=1, column=i, padx=2, pady=2)

    def generate_superI_container(self, list_room, frame):

        superI_label = ttk.Label(self.superI_frame, text="Superior I",
                                  font=("Helvetica", 14, "bold"))
        superI_label.grid(row=0, column=0, columnspan=5)

        for i, room in enumerate(list_room):
            superI_container = self.create_container(room, frame)
            #superI_container.grid(row=1, column=i, padx=2, pady=2)

            if i < 5:
                superI_container.grid(row=1, column=i, padx=2, pady=2)
            else:
                superI_container.grid(row=2, column=i-5, padx=2, pady=2, columnspan=3)
            

    def generate_superII_container(self, list_room, frame):

        superII_label = ttk.Label(self.superII_frame, text="Superior II",
                                  font=("Helvetica", 14, "bold"))
        superII_label.grid(row=0, column=0, columnspan=8)

        for i, room in enumerate(list_room):
            superII_container = self.create_container(room, frame)

            if i < 8:
                superII_container.grid(row=1, column=i, padx=2, pady=2)
            else:
                superII_container.grid(row=3, column=i-8, padx=2, pady=2)

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

        for widget in self.deluxe_frame.winfo_children():
            widget.destroy()

        self.generate_deluxe_container(self.list_deluxe_room, self.deluxe_frame)

        for widget in self.superI_frame.winfo_children():
            widget.destroy()
        self.generate_superI_container(self.list_superI_room, self.superI_frame)

        for widget in self.superII_frame.winfo_children():
            widget.destroy()
        self.generate_superII_container(self.list_superII_room, self.superII_frame)

        for widget in self.standard_frame.winfo_children():
            widget.destroy()
        self.generate_standard_container(self.list_standard_room, self.standard_frame)
        
    
    def open_booking(self, room):
        
        def callback(booking_result):
            if  booking_result=='Booked':
                self.refresher()

        booking = BookingView(self, room, self.controller, callback)

    def clean_booking(self, room):
        self.db_interaction.clean_room(room)
        self.controller.frames[GuestView.__name__].display_guests()
        self.refresher()

    def add_booking(self, room):
        def callback(booking_result):
            if  booking_result=='Booked':
                self.refresher()

        booking = BookingView(self, room, self.controller, callback, exist=True)