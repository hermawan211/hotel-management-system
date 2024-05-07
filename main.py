import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from gui.dashboardUI import *
from gui.guestsUI import *
from gui.dataUI import *

class HotelManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hotel Fatima System")

        label = ttk.Label(self, text="Hotel Mega6", font=30, background='#CDCDCD')
        label.pack(pady=20, padx=20)
    
        # Main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Navigation bar
        self.nav_bar = ttk.Frame(self.main_frame)
        self.nav_bar.pack(side=tk.TOP, fill=tk.X)

        # ------------------ Navigation buttons ------------------

        self.style = Style()
        self.style.configure('nav.TButton', font = ('calibri', 12), background='#2E2E2E', foreground="black")
        self.style.map('nav.TButton',  background=[('active', 'black')])

        # Dashboard frame
        self.dashboardPhoto = tk.PhotoImage(file='images/dashboard.png')
        self.dashboardPhoto = self.dashboardPhoto.subsample(5, 5)

        self.dashboard_btn = ttk.Button(self.nav_bar, text="Dashboard", style='nav.TButton', command=self.show_dashboard,
                                        image=self.dashboardPhoto, compound=LEFT,)
        self.dashboard_btn.pack(side=tk.LEFT, padx=(50,0), pady=(15,))
        
        # Guest frame
        self.guestPhoto = tk.PhotoImage(file='images/guest.png')
        self.guestPhoto = self.guestPhoto.subsample(5, 5)

        self.guest_btn = ttk.Button(self.nav_bar, text="Guest", style='nav.TButton', command=self.show_guest,
                                    image=self.guestPhoto, compound=LEFT)
        self.guest_btn.pack(side=tk.LEFT, padx=0,)

        # Data frame
        self.dataPhoto = tk.PhotoImage(file='images/data.png')
        self.dataPhoto = self.dataPhoto.subsample(5,5)

        self.data_btn = ttk.Button(self.nav_bar, text="Data",style='nav.TButton', command=self.show_data,
                                   image=self.dataPhoto, compound=LEFT)
        self.data_btn.pack(side=tk.LEFT, padx=0,)

        # Create a frame to hold views
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Create and store views
        self.frames={}
        for ViewClass in [DashboardView, GuestView, DataView]:
            frame = ViewClass(self.content_frame, self)
            self.frames[ViewClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start with the dashboard view
        self.show_frame(DashboardView.__name__)

    def show_dashboard(self):
        self.show_frame(DashboardView.__name__)

    def show_guest(self):
        self.show_frame(GuestView.__name__)

    def show_data(self):
        self.show_frame(DataView.__name__)

    def show_frame(self, frame_name):
        # hide all frame
        for frame in self.frames.values():
            frame.grid_remove()

        # show the requested frame
        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nswe")

        

if __name__ == "__main__":
    app = HotelManagementSystem()
    app.configure(background='#CDCDCD')
    app.state('zoomed')
    app.mainloop()