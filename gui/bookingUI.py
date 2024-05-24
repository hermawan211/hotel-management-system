import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from datetime import date
from tkcalendar import Calendar

from gui.databaseApp import *
from gui.guestsUI import *
from gui.dataUI import *

today = date.today()
today = today.strftime("%d-%m-%y")

class BookingView(tk.Frame):
    def __init__(self, parent, room, controller, callback=None, exist=None):
        super().__init__(parent)

        self.list_deluxe_room = ['A-01', 'B-01', 'B-02',]
        self.list_superI_room = ['A-101', 'A-102', 'A-103', 'A-104',
                                 'B-101', 'B-102', 'B-103', 'B-104',]
        self.list_superII_room = ['A-201', 'A-202', 'A-203', 'A-204',
                                  'B-201', 'B-202', 'B-203', 'B-204',
                                  'B-301', 'B-302', 'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                                 ]
        self.list_standard_room = ['B-309', 'B-310', 'B-311']

        self.controller = controller
        self.callback = callback
        self.exist = exist

        db_interaction = DatabaseIntraction()
        details = db_interaction.get_guest_detail(room)

        # Create parent frame for layout
        self.booking_frame = Toplevel()
        self.booking_frame.title("Booking")
        self.booking_frame.geometry("750x400")

        # Set the window position
        self.booking_frame.geometry("+{}+{}".format(270, 150))

        self.detail_frame = ttk.Frame(self.booking_frame)
        self.detail_frame.grid(row=0, column=0, padx=(180,0), sticky="nsew")

        # ------------------ Booking Details ------------------
        booking_label = ttk.Label(self.booking_frame, text="Booking Details",
                                  font=("Helvetica", 14, "bold"))
        booking_label.grid(row=0, column=0, sticky='nw')

        # date
        date_label = ttk.Label(self.detail_frame, text=today,
                               font=("Helvetica", 12, ))
        date_label.grid(row=0, column=1, sticky='e', padx=(60, 0))

        # room number
        self.room = room
        room_label = ttk.Label(self.detail_frame, text=self.room,
                                  font=("Helvetica", 12, 'bold'))
        room_label.grid(row=0, column=2,padx=(20, 0))
        
        # name
        self.name_var = tk.StringVar()
        name_label = ttk.Label(self.detail_frame, text="Name: ",
                                  font=("Helvetica", 12,))
        name_label.grid(row=1, column=0, pady=(40,0), sticky='w')

        self.name_entry = ttk.Entry(self.detail_frame, textvariable=self.name_var, font=("Helvetica", 12))
        self.name_entry.grid(row=1, column=1, padx=(40,), pady=(40,0))

        # Phone
        self.phone_var = tk.StringVar()
        phone_label = ttk.Label(self.detail_frame, text="Phone: ",
                                  font=("Helvetica", 12,))
        phone_label.grid(row=2, column=0, sticky='w')

        self.phone_entry = ttk.Entry(self.detail_frame, textvariable=self.phone_var, font=("Helvetica", 12))
        self.phone_entry.grid(row=2, column=1, padx=(40,))

        # Function for adding date for checkout
        if exist == True:
            details = db_interaction.get_guest_detail(room)
            self.name_var.set(details[0][0])
            self.phone_var.set(details[0][1])

        # Price
        self.price_var = tk.StringVar()
        price_label = ttk.Label(self.detail_frame, text="Price: ",
                                  font=("Helvetica", 12,))
        price_label.grid(row=3, column=0, sticky='w')

        self.price_entry = ttk.Entry(self.detail_frame, textvariable=self.price_var, font=("Helvetica", 12))
        self.price_entry.grid(row=3, column=1, padx=(40,))

        # Checkout date entry
        checkout_label = ttk.Label(self.detail_frame, text="Checkout Date: ",
                                    font=("Helvetica", 12,))
        checkout_label.grid(row=4, column=0,pady=(20,0), sticky='nw')

        self.cal = Calendar(self.detail_frame, selectmode= 'day',
                       year=int(today[6:]), month=int(today[3:5]), day=int(today[:2]))
        self.cal.grid(row=4, column=1, pady=(10,0))

        self.cal.bind("<<CalendarSelected>>", self.update_price_var)
        

        # Cancel
        cancel_button = ttk.Button(self.detail_frame, text="Cancel", command=self.cancel_data)
        cancel_button.grid(row=5, column=0, pady= (20,0))

        # submit
        submit_button = ttk.Button(self.detail_frame, text="Submit", command=self.submit_data)
        submit_button.grid(row=5, column=1, pady=(20,0))
        

    def cancel_data(self):
        self.booking_frame.destroy()

    def update_price_var(self, event=None):
        selected_date = self.cal.get_date()
        month, day, year = selected_date.split('/')
        self.formatted_date_str = f"{int(day):02d}-{int(month):02d}-{int(year)}"
        
        today_date = datetime.strptime(today, "%d-%m-%y").date()
        formatted_date = datetime.strptime(self.formatted_date_str, "%d-%m-%y").date()
        number_of_days = (formatted_date - today_date).days

        self.total_price = number_of_days * self.get_price()
        self.price_var.set(self.total_price)

    def get_price(self):
        if self.room in self.list_deluxe_room:
            return 250000
        elif self.room in self.list_superI_room:
            return 200000
        elif self.room in self.list_superII_room:
            return 180000
        elif self.room in self.list_standard_room:
            return 160000

    def submit_data(self,):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        dateIn = today
        dateOut = self.formatted_date_str
        price = self.total_price
        #roomCondition = 'Full'

        if name =='' or phone=='':
            messagebox.showwarning("Warning", "Please input name and phone!", parent=self.detail_frame)

        else:
            self.name_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.price_entry.delete(0, END)

            db_interaction = DatabaseIntraction()
            
            if self.exist == True:
                db_interaction.edit_data(self.room, dateOut, price)
                if self.callback:
                    self.callback("Booked")
                    messagebox.showinfo("Booking Details", "Edited!") 

            else:
                db_interaction.write_data(name, phone, dateIn, dateOut, self.room, price, "Full")
                messagebox.showinfo("Booking Details", "Successfully Booked!") 

            self.controller.frames[GuestView.__name__].display_guests()
            self.controller.frames[DataView.__name__].display_data()

            if self.callback:
                self.callback("Booked")

            self.booking_frame.destroy()