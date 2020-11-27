import math

list_of_char=[str(ch) for ch in input().split()]
str_with_no_spaces=''.join(list_of_char)
#print(str_with_no_spaces)
len_str=len(str_with_no_spaces)
r=math.floor(math.sqrt(len_str))
c=math.ceil(math.sqrt(len_str))

if r*c>=len_str:
    r=r
    c=c
elif r*c<len_str:
        r=r+1
list_of_grid=list()
s=0
for i in range(r):
    temp=str_with_no_spaces[s:s+c]
    #print(temp)
    list_of_grid.append(temp)
    s=s+c

#print(list_of_grid)
list_for_fin_ans=list()

for i in range(c):
    temp_list_for_char=list()
    for j in range(r):
        temp_word=list_of_grid[j]
        l=len(temp_word)

        if l>i:
            let=temp_word[i]
            temp_list_for_char.append(let)
        elif l<=i:
            continue
    list_for_fin_ans.append(''.join(temp_list_for_char))

ans=' '.join(list_for_fin_ans)
print(ans)
