#finding the average
def average():

    student={"mythili":[10,20,30],
             "priya":[40,50,20],
             "aruna":[80,20,40]
             }

    student_name=input("enter the student name: ")

    mark=student[student_name]

    total=0

    for i in mark:
        total+=i

    avg=total/3
    print(avg)


