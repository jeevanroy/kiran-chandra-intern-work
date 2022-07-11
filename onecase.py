from reportlab.pdfgen import canvas
import random

n = int(input("How many number of rectangles do you need?: "))

c = canvas.Canvas("pdf_table{4}.pdf", pagesize=(1000,1000))

if n==1:
    w1 = random.randrange(900)
    h1 = random.randrange(900)
    c.rect(500,500,w1,h1)
    print(500,500,w1,h1)
    c.save()
