l=[int(n) for n in input().split()]
l.sort()

min_sum=sum(l[:4])
max_sum=sum(l[1:])
print(min_sum,max_sum)
