num_student = int(input("Enter how many students you want: "))

student_name = []

for i in range(num_student):
    name = input("Enter student name: ")
    student_name.append(name)

total_students = len(student_name)

print(student_name)
print("Total students:", total_students)


