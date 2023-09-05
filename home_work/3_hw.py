def func1 (x,y):
    if x>y:
        print(x)
    elif x<y:
        print (y)
func1(3,5)
def func2 (x,y):
    if x-y == 135 or y-x == 135:
        print('YES')
    else:
        print('NO')
func2(136,1)
def func3 (x):
    if x in  (1,2,12):
        print ('Зима')
    elif x in range (3,6):
        print ('Весна')
    elif x in range (6,9):
        print ('Лето')
    elif x in range (9,12):
        print ('Осень')
func3(7)
def func4(x,y,z):
    if x>10 and y>10 and z>10:
        print ('Yes')
    else:
        print ('No')
func4(9,10,11)
def func5(x):
    a=0
    for c in x:
        if c>0:
            a+=1
    print(a)
g=[1,2,-5,-4,5]
func5(g)
def func6(x,y):
    c = 0
    c = (x * 12 * 29) + (y*29)
    print(c)
func6(3,5)
