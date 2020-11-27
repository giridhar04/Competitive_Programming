def simpleArraySum(ar):
    sum_arr=sum(ar)
    return sum_arr

n=int(input())
ar=[int(n) for n in input().split()]

ans=simpleArraySum(ar)
print(ans)
