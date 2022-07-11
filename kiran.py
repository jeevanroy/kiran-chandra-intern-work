from reportlab.pdfgen import canvas
import random

n = int(input("How many number of rectangles do you need?: "))

c = canvas.Canvas("pdf_table{4}.pdf", pagesize=(1000,1000))

for k1 in range(int(n**0.5+1)):
    if k1**2 == n:
        print(k1)
        k=k1

x=[' ']*(k+1)
k_part = 0

while (k_part<k+1):
    x[k_part]=int(k_part*(1000/k))
    k_part+=1

print(x)
y = x

xy_tups = []
ci=0
while (ci<len(x)-1):
    if ci==(len(x)-1):
        xi = (x[ci-1]+x[ci])/2
        yi = (y[ci-1]+y[ci])/2
        xy_tups.append((int(xi),int(yi)))
    else:
        xi = (x[ci]+x[ci+1])/2
        yi = (y[ci]+y[ci+1])/2
        xy_tups.append((int(xi),int(yi)))

    ci+=1

x_center = []
for ele in xy_tups:
    x_center.append(ele[0])

y_center = []
for ele in xy_tups:
    y_center.append(ele[1])

print("x center:" ,x_center)
print("y center",y_center)



for ele_x in x_center:
    for ele_y in y_center:
         w = random.randrange(0,int(1000/k))
         h = random.randrange(0,int(1000/k))
         c.rect(ele_x,ele_y,w,h)
         print(ele_x,ele_y,w,h)


c.save()
print("Pdf generated....")
