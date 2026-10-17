class Student:
    def display(self):
        print("Name:", self.student_name)
        print("Roll number:", self.student_id)

student_obj = Student()
student_obj.student_name = "Rahul"
student_obj.student_id = 101
student_obj.display()
