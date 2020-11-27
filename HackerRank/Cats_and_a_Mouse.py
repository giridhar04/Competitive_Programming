n=int(input())

for i in range(n):
    x,y,z=[int(var) for var in input().split()]

    if abs(x-z)>abs(y-z):
        print("Cat B")
    elif abs(x-z)<abs(y-z):
        print("Cat A")
    else:
        print("Mouse C")
