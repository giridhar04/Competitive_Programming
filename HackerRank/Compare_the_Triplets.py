def compareTriplets(a,b):
    l=[0,0]

    for i in range(len(a)):
        if a[i]>b[i]:
            l[0]=l[0]+1
        elif a[i]<b[i]:
            l[1]=l[1]+1
        else:
            l[0]=l[0]+0
            l[1]=l[1]+0
    return l

a=[int(n) for n in input().split()]
b=[int(n) for n in input().split()]

res=compareTriplets(a,b)

print(res[0],res[1])
