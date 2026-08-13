class StudentDatabase:
    student_list = [] 

    @classmethod
    def add_student(self,stdnt_info):
        self.student_list.append(stdnt_info) 

class Student:
    def __init__(self,id,name,department,is_enrolled):
        self.id = id
        self.name = name
        self.dep = department
        self.enrolled = is_enrolled
    def enroll_student(self,id):
        if self.enrolled == False:
            self.enrolled = True

    def drop_student(self,id):
        self.enrolled = False

            
    def view_student_info(self):
        print(f'ID: {self.id}, Name: {self.name}, Department: {self.dep}, Enrolled: {self.enrolled}')
        
      
# stn = StudentDatabase()
student1 = Student(101,'Afnan Nishu','CSE',True)
student2 = Student(102,'Mahia Mahi','CSE',False)
student3 = Student(103,'Mehjabeen','CSE',True)

StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)
StudentDatabase.add_student(student3)

# for student in stn.student_list:
#     student.view_student_info()

def user():

    while True:
        print('\n---- Student Management Menu ----')
        print('1. View all Students')
        print('2. Enroll Student')
        print('3. Drop Student')
        print('4. Exit')

        choice = int(input('Enter your choice (1-4) : '))
        if choice == 1:
            if len(StudentDatabase.student_list) != 0:
                for students in StudentDatabase.student_list:
                    students.view_student_info()
            else:
                print('No student enrolled')
        
        elif choice == 2:
            id = int(input('Enter student ID : '))
            flag = -1
            for student_id in StudentDatabase.student_list:
                if student_id.id == id:
                    flag = 1
                    if student_id.enrolled == False:
                        student_id.enroll_student(id)
                        print(f'{student_id.id} has enrolled')
                        break
                    elif student_id.enrolled == True:
                        print(f'{student_id.id} is already enrolled')
                        break

            if flag == -1:
                print('Invalid Student ID')

        elif choice == 3:
            id = int(input('Enter student ID : '))
            flag = -1
            for student_id in StudentDatabase.student_list:
                if student_id.id == id:
                    flag = 1
                    if student_id.enrolled == True:
                        student_id.drop_student(id)
                        print(f'{student_id.id} has dropped')
                        break
                    elif student_id.enrolled == False:
                        print(f'{student_id.id} is already dropped')
                        break

            if flag == -1:
                print('Invalid Student ID')

        elif choice == 4:
            print('Thank You..')
            break
        else:
            print('Invalid choice.')

user()