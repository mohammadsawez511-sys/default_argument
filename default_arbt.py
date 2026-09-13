def result_of_student(name, roll_number, marks, name_of_college="ATT HIGH SCHOOL"):
    print("name =", name)
    print("roll number =", roll_number)
    print("total marks =", sum(marks))
    print("percentage =", sum(marks) / (len(marks)))
    print("college =", name_of_college)

result_of_student("sawez", 22, [45, 45],)
