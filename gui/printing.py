from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

myCanvas = canvas.canvas('receipt.pdf', pagesize=A4)
width, height = A4

list_deluxe_room = ['A-01', 'B-01', 'B-02',]
list_superI_room = ['A-101', 'A-102', 'A-103', 'A-104',
                            'B-101', 'B-102', 'B-103', 'B-104',]
list_superII_room = ['A-201', 'A-202', 'A-203', 'A-204',
                            'B-201', 'B-202', 'B-203', 'B-204',
                            'B-301', 'B-302', 'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                            ]
list_standard_room = ['B-309', 'B-310', 'B-311']

def write_pdf(name, phone, date, dateIn, dateOut, room, price):
    print(name, phone)