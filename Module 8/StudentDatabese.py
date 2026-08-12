class StudentDatabase:
    student_list = [] 
    @classmethod
    def add_student(self,name,department):
        id = len(self.student_list) + 101
        student = Student(name,id,department,True)
        self.student_list.append(student) 

class Student:
    def __init__(self,id,name,department,is_enrolled):
        self.id = id
        self.name = name
        self.dep = department
        self.enrolled = is_enrolled
    def enroll_student(self):
        if self.enrolled == False:
            self.enrolled = True
        else:
            print(f'{self.name} is already enrolled')
    def drop_student(self):
        self.enrolled = False
    def view_student_info(self):
  
        print(f'ID: {self.id}, Name: {self.name}, Department: {self.dep}, Enrolled: {self.enrolled}')
      
stn = StudentDatabase()
stn.add_student('minhaj','cse')
stn.add_student('rakin','cse')

for student in stn.student_list:
    student.view_student_info()