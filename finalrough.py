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
    print('Pdf generated...')

if n==2:
    w1 = random.randrange(800)
    h1 = random.randrange(500)
    c.rect(500,250,w1,h1)
    print(500,250,w1,h1)

    w1 = random.randrange(800)
    h1 = random.randrange(500)
    c.rect(500,750,w1,h1)
    print(500,750,w1,h1)
    c.save()
    print('Pdf generated...')

def even_number():
    if n%2==0 and n!=2:
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


    main_coords = []
    for ele_x in x_center:
        for ele_y in y_center:
             w = random.randrange(0,int(1000/k))
             h = random.randrange(0,int(1000/k))
             c.rect(ele_x,ele_y,w,h)
             #print(ele_x,ele_y,w,h)

             main_coords.append((ele_x,ele_y,w,h))

    print('-'*100)
    print('-'*100)
    print('main_coords : {}'.format(main_coords))

    c.save()
    print("Pdf generated....")

def odd_number():
    if n%2!=0 and n!=1:
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


    upper_main_coords = []
    for ele_xu in x_ucenter:
             w = random.randrange(0,int(1000/k))
             h = random.randrange(0,int(1000/k))
             c.rect(ele_xu,750,w,h)
             #print(ele_xu,750,w,h)
             upper_main_coords.append((ele_xu,750,w,h))

    print('-'*100)
    print('-'*100)
    print('upper main_coords : {}'.format(upper_main_coords))

    lower_main_coords = []
    for ele_xl in x_lcenter:
             w = random.randrange(0,int(1000/(k+1)))
             h = random.randrange(0,int(1000/(k+1)))
             c.rect(ele_xl,250,w,h)
             #print(ele_xl,250,w,h)
             lower_main_coords.append((ele_xl,250,w,h))

    print('-'*100)
    print('-'*100)
    print('lower main_coords : {}'.format(lower_main_coords))

    c.save()
    print("Pdf generated....")

def square_number():
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

    main_coords = []
    for ele_x in x_center:
        for ele_y in y_center:
             w = random.randrange(0,int(1000/k))
             h = random.randrange(0,int(1000/k))
             c.rect(ele_x,ele_y,w,h)
             #print(ele_x,ele_y,w,h)
             main_coords.append((ele_x,ele_y,w,h))

    print('-'*100)
    print('-'*100)
    print('main_coords : {}'.format(main_coords))



    c.save()
    print("Pdf generated....")

if n%2==0 and n!=2:
    kk=n
    for k1 in range(int(n**0.5+1)):
        if k1**2 == n:
            kk=k1
            square_number()
    if kk==n:
        even_number()


if n%2!=0 and n!=1:
    kk=n
    for k1 in range(int(n**0.5+1)):
        if k1**2 == n:
            kk=k1
            square_number()
    if kk==n:
        odd_number()
