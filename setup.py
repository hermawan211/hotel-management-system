from cx_Freeze import setup, Executable

setup(
    name="HotelManagementSystem",
    version="1.0",
    description="Hotel Management System",
    executables=[Executable("main.py")]
)