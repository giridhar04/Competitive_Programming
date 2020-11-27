def plusMinus(arr):
    n=len(arr)
    neg_count=len(list(filter(lambda x: (x<0),arr)))
    pos_count=len(list(filter(lambda x: (x>0),arr)))
    zero_count=n-(neg_count+pos_count)

    pos=round(pos_count/n,6)
    neg=round(neg_count/n,6)
    zer=round(zero_count/n,6)

    return pos,neg,zer

n=int(input())
arr=[int(i) for i in input().split()]

res=list(plusMinus(arr))

for i in range(len(res)):
    temp=res[i]
    print('{:.6f}'.format(temp))
