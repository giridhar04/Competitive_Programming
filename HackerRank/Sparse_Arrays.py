nu_str=int(input())
list_of_str=list()

for i in range(nu_str):
    temp=input()
    list_of_str.append(temp)

no_query_str=int(input())
list_of_query_str=list()

for i in range(no_query_str):
    temp=input()
    count=0
    for string in list_of_str:
        if string==temp:
            count+=1
    print(count)
