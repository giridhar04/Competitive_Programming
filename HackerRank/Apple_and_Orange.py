def countApplesAndOranges(s,t,dist_app,dist_ora):
    count_app=0
    count_ora=0

    for i in range(len(dist_app)):
        if s<= dist_app[i] <= t:
            count_app=count_app+1
        else:
            continue
    for j in range(len(dist_ora)):
        if s<= dist_ora[j]<=t:
            count_ora=count_ora+1
        else:
            continue
    return count_app,count_ora

s,t=[int(n) for n in input().split()]
a, b = [int(n) for n in input().split()]
m, n = [int(n) for n in input().split()]
dist_app = [int(n)+a for n in input().split()]
dist_ora = [int(n)+b for n in input().split()]

ans_1,ans_2=countApplesAndOranges(s,t,dist_app,dist_ora)

print(ans_1)
print(ans_2)
