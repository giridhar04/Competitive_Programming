def gradingStudents(grades):

    new_list=list()

    for grade in grades:
        new_grade=grade+(5-(grade%5))

        if (new_grade-grade)<3:

            if new_grade>=40:
                grade=new_grade
                new_list.append(grade)
            else:
                new_list.append(grade)
        else:
            new_list.append(grade)

    return new_list

n=int(input())
grades=list()

for i in range(n):
    temp=int(input())
    grades.append(temp)

res=gradingStudents(grades)

for i in range(n):
    print(res[i])
