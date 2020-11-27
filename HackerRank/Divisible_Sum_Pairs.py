#divisible sum pairs

n,k=[int(var) for var in input().split()]

num=[int(var) for var in input().split()]
count=0

for i in range(0,n-1):
    for j in range(1,n):
        #print("num[i]:", num[i], "num[j]:", num[j])
        temp=num[i]+num[j]
        if (i<j) and temp%k==0:
            count+=1
print(count)
