#day of the programmer

year=int(input())

if 1700<=year<=1917:

    if year%4==0:
        year=str(year)
        print("12.09."+year)
    else:
        year=str(year)
        print("13.09."+year)
elif year==1918:
    year=str(year)
    print("26.09."+year)
elif year>1918:
    if (year%400==0) or ((year%4==0) and (year%100!=0)):
        year=str(year)
        print("12.09."+year)
    else:
        year=str(year)
        print("13.09."+year)
