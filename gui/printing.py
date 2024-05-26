from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

list_deluxe_room = ['A-01', 'B-01', 'B-02',]
list_superI_room = ['A-101', 'A-102', 'A-103', 'A-104',
                            'B-101', 'B-102', 'B-103', 'B-104',]
list_superII_room = ['A-201', 'A-202', 'A-203', 'A-204',
                            'B-201', 'B-202', 'B-203', 'B-204',
                            'B-301', 'B-302', 'B-303', 'B-304', 'B-305', 'B-306', 'B-307', 'B-308',
                            ]
list_standard_room = ['B-309', 'B-310', 'B-311']

def write_pdf(name, phone, date, dateIn, dateOut, room, price):
    myCanvas = canvas.Canvas('receiptest.pdf', pagesize=landscape(A4))
    width, height = landscape(A4)

    # Draw the background image
    myCanvas.drawImage('images/Logo.jpg', 0, -160, width=width, height=height + 300)

    # Title
    title_text = "Hotel MEGA 6"
    myCanvas.setFont("Helvetica-Bold", 36)
    title_width = myCanvas.stringWidth(title_text, "Helvetica-Bold", 36)
    x_position = (width - title_width) / 2

    myCanvas.drawString(x_position, height - 100, title_text)

    # Receipt
    receipt_text = "Receipt"
    myCanvas.setFont("Helvetica-Bold", 22)
    receipt_width = myCanvas.stringWidth(receipt_text, "Helvetica-Bold", 22)
    x_position = (width - receipt_width) / 2

    myCanvas.drawString(x_position, height - 140, receipt_text)

    # Details
    myCanvas.setFont("Helvetica-Bold", 18)
    myCanvas.drawString(width - 750, height - 200, "Name           :")
    myCanvas.drawString(width - 630, height - 200, name)

    myCanvas.drawString(width - 380, height - 200, "Date    :")
    myCanvas.drawString(width - 280, height - 200, date)

    myCanvas.drawString(width - 750, height - 225, "Phone          :")
    myCanvas.drawString(width - 630, height - 225, phone)

    myCanvas.drawString(width - 750, height - 250, "Check In      :")
    myCanvas.drawString(width - 630, height - 250, dateIn)

    myCanvas.drawString(width - 750, height - 275, "Check Out   :")
    myCanvas.drawString(width - 630, height - 275, dateOut)

    myCanvas.setLineWidth(3)
    myCanvas.line(width - 750, height - 303, width - 130, height - 303)
    myCanvas.drawString(width - 750, height - 320, "Room    Type")
    myCanvas.drawString(width - 230, height - 320, "Price")
    myCanvas.line(width - 750, height - 327, width - 130, height - 327)

    myCanvas.drawString(width - 750, height - 355, room)
    myCanvas.drawString(width - 680, height - 355, get_type(room))
    myCanvas.drawString(width - 230, height - 355, price)
    myCanvas.line(width - 750, height - 375, width - 130, height - 375)

    myCanvas.setLineWidth(2)
    myCanvas.line(width - 250, height - 500, width - 130, height - 500)
    myCanvas.drawString(width - 230, height - 530, "Signature")

    myCanvas.showPage()
    myCanvas.save()

    print("Hereee")

def get_type(room):
    if room in list_deluxe_room:
        return "DELUXE"
    elif room in list_superI_room:
        return "SUPERIOR I"
    elif room in list_superII_room:
        return "SUPERIOR II"
    elif room in list_standard_room:
        return "STANDARD"