class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        
    def display_student_details(self):
        print(f"Name : {self.name}")
        print(f"Rollno : {self.rollno}")
        print(f"Marks : {self.marks}")

    def update_marks(self,new_marks):
        self.marks = new_marks
        print(f"Marks updated to : {self.marks}")
        
#student objects
stud1 = Student("Mitali",26,95)
stud2 = Student("Ragini",32,97)
stud3 = Student("Anjali",27,88)

print(" Student 1 Details :")
stud1.display_student_details()

print("\n Stduent 2 Details :")
stud2.display_student_details()

print("\n Student 3 Details :")
stud3.display_student_details()

print("\n Updating marks for Student 1, Student 2 and Student 3 as : ")
stud1.update_marks(99)
stud2.update_marks(90)
stud3.update_marks(81)

print("\n Updated Student 1 Details : ")
stud1.display_student_details()
print("\n Updated Student 2 Details : ")
stud2.display_student_details()
print("\n Updated Student 3 Details : ")
stud3.display_student_details()



