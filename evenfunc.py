def even_number

if n%2==0:
    k=int(n/2)

x=[' ']*(k+1)
k_part = 0

while (k_part<k+1):
    x[k_part]=int(k_part*(1000/k))
    k_part+=1

print(x)

y_center=[250,750]

x_center=[]

ci=0
while (ci<len(x)-1):
    if ci==(len(x)-1):
        xi = (x[ci-1]+x[ci])/2
        x_center.append(xi)
    else:
        xi = (x[ci]+x[ci+1])/2
        x_center.append(xi)

    ci+=1

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
