d1,m1,y1=[int(var) for var in input().split()]
d2,m2,y2=[int(var) for var in input().split()]


if(y1>y2):
    print("10000")
elif (y1<y2):
    print("0")
elif(y1==y2):
    if(m1>m2):
        print(500*(m1-m2))
    elif(m1<m2):
        print("0")
    elif(m1==m2):
        if(d1>d2):
            print(15*(d1-d2))
        elif(d1<=d2):
            print("0")
