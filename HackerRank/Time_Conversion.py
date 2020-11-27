l=[var for var in input().split(':')]
h_12=int(l[0])
f_12=l[2][2:]
l_24=list()

if f_12=="AM":
    if h_12==12:
        l_24.append("00")
        l_24.append(l[1])
        l_24.append(l[2][:2])
        ans=':'.join(l_24)
    else:
        l_24.append(l[0])
        l_24.append(l[1])
        l_24.append(l[2][:2])
        ans=':'.join(l_24)
elif f_12=="PM":
    if h_12==12:
        l_24.append("12")
        l_24.append(l[1])
        l_24.append(l[2][:2])
        ans=':'.join(l_24)
    else:
        h_24=12+h_12
        l_24.append(str(h_24))
        l_24.append(l[1])
        l_24.append(l[2][:2])
        ans=':'.join(l_24)
print(ans)
