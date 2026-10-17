with open("student.txt", "w") as student_file:
    student_file.write("Name: Rahul\nCourse: BCA\n")
with open("student.txt", "r") as student_file:
    print(student_file.read())
