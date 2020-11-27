size_alp=list(map(int,input().split()))
string=input()
size_of_chars=list()

dict_let=dict()
#print(size_alp)
var = 97
for num in size_alp:
    dict_let[chr(var)]=num
    var+=1
#print(dict_let)
for char in string:
    temp=dict_let[char]
    size_of_chars.append(temp)

print(max(size_of_chars)*len(string))
