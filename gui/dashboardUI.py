import tkinter as tk
from tkinter import ttk

class DashboardView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Create parent frame for layout
        self.dashboard_frame = ttk.Frame(self)
        self.dashboard_frame.pack(fill="both", expand=True)

        # ------------------ Premium Frame ------------------
        premium_frame = ttk.Frame(self.dashboard_frame)
        premium_frame.pack(fill='x', padx=10, pady= 5)

        premium_label = ttk.Label(premium_frame, text="Premium Room",
                                  font=("Helvetica", 14, "bold"))
        premium_label.pack(fill="x", padx=200, pady=5)

        list_premium_room = ['A-01', 'A-101', 'A-102', 'A-103', 'A-104',
                             'A-201', 'A-202', 'A-203', 'A-204']

        self.generate_premium_container(list_premium_room, premium_frame)
        
        # ------------------ Standart Frame ------------------
        standart_frame = ttk.Frame(self.dashboard_frame)
        standart_frame.pack(fill='x', padx=10, pady= 5)

        standart_label = ttk.Label(standart_frame, text="Standart Room",
                                  font=("Helvetica", 14, "bold"))
        standart_label.pack(fill="x", padx=200, pady=5, anchor="center")

        list_standart_room = ['B-01', 'B-02','B-101', 'B-102', 'B-103', 'B-104',
                             'B-201', 'B-202', 'B-203', 'B-204', 'B-301', 'B-302',
                             'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                             'B-309', 'B-310', 'B-311']

        self.generate_standard_container(list_standart_room, standart_frame)

    def generate_premium_container(self, list_room, frame):
        for i in list_room:
            premium_container = self.create_container(i, frame)
            premium_container.pack(fill="x", padx=10, pady=0)
            

    def generate_standard_container(self, list_room, frame):
        pass

    def create_container(self, list_room, frame):
        container = ttk.Frame(frame)

        room_label = ttk.Label(container, text=list_room, font=("Helvetica", 10, "bold"))
        room_label.pack(side="left", padx=(0, 10))

        return container