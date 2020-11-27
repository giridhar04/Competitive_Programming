#staircase

n=int(input())
for i in range(1,n+1):
    temp1=[' ']*(n-i)
    temp2=['#']*i
    temp=temp1+temp2
    print(''.join(temp))
