dict_of_time = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen',18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three ', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine',30:'past',45:'quarter'}
hour=int(input())
min=int(input())

if min==0:
    print(dict_of_time[hour],"o' clock")
elif min==1:
    print("one minute past",dict_of_time[hour])
elif min==15:
    print("quarter past",dict_of_time[hour])
elif min==30:
    print("half past",dict_of_time[hour])
elif min==45:
    print("quarter to",dict_of_time[hour+1])
elif min==59:
    print("one minute to",dict_of_time[hour+1])
else:
    if min<30:
        print(dict_of_time[min],"minutes past",dict_of_time[hour])
    elif min>30:
        min=60-min
        print(dict_of_time[min],"minutes to",dict_of_time[hour+1])
