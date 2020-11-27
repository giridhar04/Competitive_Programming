#electronic shop

budg,n_key,n_usb=[int(var) for var in input().split()]
mon_key=[int(var) for var in input().split()]
mon_usb=[int(var) for var in input().split()]
l=list()

for item_1 in mon_key:
    for item_2 in mon_usb:
        if (item_1+item_2)<=budg:
            l.append(item_1+item_2)
if len(l)>0:
    print(max(l))
elif len(l)==0:
    print("-1")
