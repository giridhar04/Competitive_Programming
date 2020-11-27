#Non divisible subset
def solveSubset(S, k, n):
    r = [0] * k    #remainder list to store number of numbers with particular remainder

    for value in S:
        r[value % k] += 1 #counting numbers based on remainder
    #print(r)
    result = 0
    for a in range(1, (k+1)//2): #traverse list upto middle of r
        result += max(r[a], r[k-a]) #take into account the maximum numbers among r[k] and r[k-a]
    if k % 2 == 0 and r[k//2]: #if k is even then we will miss one position in the above loop
        result += 1
    if r[0] !=0: #we can take only one number with remainder zero according to question
        result += 1
    return result


n, k = map(int, input().split())
S = map(int, input().split())
print(solveSubset(S, k, n))
