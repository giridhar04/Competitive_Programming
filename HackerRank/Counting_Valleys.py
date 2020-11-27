#counting valleys

import math

n=int(input())
steps=list(input())
curr_level=0
prev_level=0
valley=0

for step in steps:

    if step=="U":
        curr_level+=1
    elif step=="D":
        curr_level-=1
    #print("curr_lev:",curr_level)
    sign_curr=math.copysign(1,curr_level)
    sign_prev=math.copysign(1,prev_level)
    #print("sign_curre:",sign_curr,"sign_prev",sign_prev)

    if (sign_curr==-1) and (sign_prev==1):
        valley+=1
    prev_level=curr_level
print(valley)
