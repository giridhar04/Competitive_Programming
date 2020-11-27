def kangaroo(x1,v1,x2,v2):
    
    if v1<=v2:
       ans="NO"
    elif v1>v2:
        n = (x1-x2)/(v2-v1)+1
        if n==int(n):
            ans="YES"
        else:
            ans="NO"
    
    return ans

x1,v1,x2,v2=[int(n) for n in input().split()]
result=kangaroo(x1,v1,x2,v2)
print(result)
