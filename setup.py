from cx_Freeze import setup, Executable

build_exe_options = {
    "include_files": [
        "images",
        "receipt.pdf"
    ]
}

setup(
    name="HotelManagementSystem",
    version="2.0",
    description="Hotel Management System",
    options = {"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)