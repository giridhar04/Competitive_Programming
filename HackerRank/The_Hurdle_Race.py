n,k=[int(var) for var in input().split()]
heights=[int(var) for var in input().split()]

max_hei=max(heights)
tot=0

if k>=max_hei:
    print(tot)
else:
    tot=max_hei-k
    print(tot)
    
