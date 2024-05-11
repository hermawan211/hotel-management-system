
from gui.guestsUI import *
from gui.dataUI import *

class RefreshController():
    def __init__(self, controller):
        self.controller = controller

    def refresh_guests(self):
        self.controller.frames[GuestView.__name__].display_guests()

    def refresh_data(self):
        self.controller.frames[DataView.__name__].display_data()