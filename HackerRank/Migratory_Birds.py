#bird count

n=int(input())
bird_seen=list(map(int,input().split()))
act_bird_type=[1,2,3,4,5]
count=[0,0,0,0,0]

for i in range(5):
    count[i]=bird_seen.count(act_bird_type[i])
max_c=max(count)

print(count.index(max_c)+1)
