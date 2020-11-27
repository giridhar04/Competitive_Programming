import math

n=int(input())
shar=5
likes=0

for i in range(n):
    var_likes=math.floor(shar/2)
    shar=var_likes*3
    likes+=var_likes
print(likes)
