'''
OPTIMISED VERSION of the finalrough.py file.
That can generate rectangles without compromising the space in the 1000x1000 pagesize.

Try n=98,99,100,101,102 in both the finalrough.py and this file.
You can notice the optimization.

Explanation:
    According to the finalrough.py file you are saying that n = even, odd, perfect_square, odd, and even.
    But According to this file you are asking for n=100-2,100-1,100,100+1,100+2.

'''

from reportlab.pdfgen import canvas
import random

n = int(input("How many number of rectangles do you need?: "))

c = canvas.Canvas("pdf_table{4}.pdf", pagesize=(1000,1000))


def perfect_square(n):

    '''
    #a function to check whether n is a perfect square or not.
    #The below function returns True if n is a perfect sqauare and False if n is not a perfect square.
    '''

    i=1
    while (i<n+1):
        if i**2==n:
            global i_val
            i_val = i
            return True
        i+=1
    else:
        return False


def perfect_square_rect():
    '''
    #The below function is called when n is a percect square of some number.
    #A function to generate k by k grid and generate rectangles in them that did not overlap each other.
    '''

    x=[' ']*(k+1)
    k_part = 0

    while (k_part<k+1):
        x[k_part]=int(k_part*(1000/k))
        k_part+=1
    print('.'*100)
    print('.'*100)
    print('Vertical Lines Which Are Rectangles Borders',x)
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


    print('-'*100)
    print('-'*100)
    print("x center:" ,x_center)
    print('-'*100)
    print('-'*100)
    print("y center",y_center)


    main_coords = []
    for ele_x in x_center:
        for ele_y in y_center:
             w = random.randrange(0,int(1000/k))
             h = random.randrange(0,int(1000/k))
             c.rect(ele_x,ele_y,w,h)
             main_coords.append((ele_x,ele_y,w,h))
    print('-'*100)
    print('-'*100)
    print('MAIN COORDINATES LIST',main_coords)
    print('_'*100)
    print('_'*100)
    print('Length of the main_coords list',len(main_coords))
    print('-'*100)
    print('-'*100)


    c.save()
    print("Pdf generated....")
    print('.'*100)
    print('.'*100)


def not_a_perfect_square():
    '''
    #This function is called when n is NOT a percect square of some number.
    #A function to generate n number of rectangles.
    #plotting rectangles starts from origin and goes along x axis.
    #i)if we want to generate 8 rectangles then 3x3 grid will be generated and
    #ii)rectangles are plotted inside each grid with random dimensions.
    #iii)Ex:1st rectangle with center (x1,y1) then ,(x2,y1),(x3,y1),etc...
    #2 Rectangles: (x1,y3),(x2,y3),*( x3,y3) THIS RECTANGLE WILL NOT BE PLOTTED*  #line eqn: y3=constant
    #3 Rectangles: (x1,y2),(x2,y2),(x3,y2)                                        #line eqn: y2=constant
    #3 Rectangles: (x1,y1),(x2,y1),(x3,y1)                                        #line eqn: y1=constant
    #iv)Total 8 centers for 8 rectangles.
    '''

    x=[' ']*(k+1)
    k_part = 0

    while (k_part<k+1):
        x[k_part]=int(k_part*(1000/k))
        k_part+=1
    print('.'*100)
    print('.'*100)
    print('Vertical Lines Which Are Rectangles Borders',x)
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


    print('-'*100)
    print('-'*100)
    print("x center:" ,x_center)
    print('-'*100)
    print('-'*100)
    print("y center",y_center)


    main_coords = []
    break_val = 1
    for ele_y in y_center:
        for ele_x in x_center:

    #for ele_x in x_center:
        #for ele_y in y_center:
            if break_val<n+1:
                w = random.randrange(0,int(1000/k))
                h = random.randrange(0,int(1000/k))
                c.rect(ele_x,ele_y,w,h)
                main_coords.append((ele_x,ele_y,w,h))
                break_val+=1

    print('-'*100)
    print('-'*100)
    print('MAIN COORDINATES LIST',main_coords)
    print('-'*100)
    print('-'*100)
    print('Length of the main_coords list',len(main_coords))
    print('-'*100)
    print('-'*100)


    c.save()
    print("Pdf generated....")
    print('.'*100)
    print('.'*100)


#if n is a perfect square then run the "if block" otherwise run the "else block"
#if n is a perfect square k by k grid will be gerated where k**2==n Ex: n=100 then k=10
#if n is NOT a perfect square then k by k grid will be generated where (k**2)-(constant)==n
#Ex: i) n=98 then k=10 and constant = 2 -> (10**2)-2==98
#Ex: i) n=99 then k=10 and constant = 1 -> (10**2)-1==99
#Ex: i) n=100 then k=10 PERFECT SQUARE i.e., 10**2==100
#Ex: i) n=101 then k=11 and constant = 20 -> (11**2)-20==101
#Ex: i) n=102 then k=11 and constant = 19 -> (11**2)-19==102

if perfect_square(n):
    k=i_val
    perfect_square_rect()
    #print(i_val)

else:
    i_list = [i for i in range(int(n**0.5+1))]
    i_val = i_list[-1]+1

    #print(i_val)
    k=i_val
    not_a_perfect_square()
