from reportlab.pdfgen import canvas
import random

n = int(input("How many number of rectangles do you need?: "))

c = canvas.Canvas("pdf_table{4}.pdf", pagesize=(1000,1000))

if n%2!=0:
    k=int(n/2)

x_upper=[' ']*(k+1)
x_lower=[' ']*(k+2)

k_part = 0

while (k_part<k+1):
    x_upper[k_part]=int(k_part*(1000/k))
    k_part+=1

k_part=0

while (k_part<k+2):
    x_lower[k_part]=int(k_part*(1000/(k+1)))
    k_part+=1

print('x upper: ',x_upper)
print('x lower: ',x_lower)

x_ucenter = []
x_lcenter = []

ci=0
while (ci<len(x_upper)-1):
    if ci==(len(x_upper)-1):
        xi = (x_upper[ci-1]+x_upper[ci])/2
        x_ucenter.append(xi)
    else:
        xi = (x_upper[ci]+x_upper[ci+1])/2
        x_ucenter.append(xi)

    ci+=1

print("x ucenter:" ,x_ucenter)
print("y ucenter",750)

ci=0
while (ci<len(x_lower)-1):
    if ci==(len(x_lower)-1):
        xi = (x_lower[ci-1]+x_lower[ci])/2
        x_lcenter.append(xi)
    else:
        xi = (x_lower[ci]+x_lower[ci+1])/2
        x_lcenter.append(xi)

    ci+=1

print("x lcenter:" ,x_lcenter)
print("y lcenter",250)



for ele_xu in x_ucenter:
         w = random.randrange(0,int(1000/k))
         h = random.randrange(0,int(1000/k))
         c.rect(ele_xu,750,w,h)
         print(ele_xu,750,w,h)

for ele_xl in x_lcenter:
         w = random.randrange(0,int(1000/(k+1)))
         h = random.randrange(0,int(1000/(k+1)))
         c.rect(ele_xl,250,w,h)
         print(ele_xl,250,w,h)


c.save()
print("Pdf generated....")
