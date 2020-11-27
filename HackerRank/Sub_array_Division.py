n=int(input())
cho_num=[int(var) for var in input().split()]
d,m=[int(var) for var in input().split()]
count,i=0,0

for i in range(0,n-m+1):
    temp=cho_num[i:i+m]
    #print(temp)
    if sum(temp)==d:
        count+=1
print(count)
