class StudentDatabase:
    student_list = [] 

    @classmethod
    def add_student(self,stdnt_info):
        self.student_list.append(stdnt_info) 

class Student:
    def __init__(self,id,name,department,is_enrolled):
        self.__id = id
        self.__name = name
        self.__dep = department
        self.__enrolled = is_enrolled

    def get_id(self):
        return self.__id
    def get_enroll(self):
        return self.__enrolled

    def enroll_student(self,id):
        if self.__enrolled == False:
            self.__enrolled = True

    def drop_student(self,id):
        self.__enrolled = False

            
    def view_student_info(self):
        print(f'ID: {self.__id}, Name: {self.__name}, Department: {self.__dep}, Enrolled: {self.__enrolled}')
        
      
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
                if student_id.get_id() == id:
                    flag = 1
                    if student_id.get_enroll() == False:
                        student_id.enroll_student(id)
                        print(f'{student_id.get_id()} has enrolled')
                        break
                    elif student_id.get_enroll() == True:
                        print(f'{student_id.get_id()} is already enrolled')
                        break

            if flag == -1:
                print('Invalid Student ID')

        elif choice == 3:
            id = int(input('Enter student ID : '))
            flag = -1
            for student_id in StudentDatabase.student_list:
                if student_id.get_id() == id:
                    flag = 1
                    if student_id.get_enroll() == True:
                        student_id.drop_student(id)
                        print(f'{student_id.get_id()} has dropped')
                        break
                    elif student_id.get_enroll() == False:
                        print(f'{student_id.get_id()} is already dropped')
                        break

            if flag == -1:
                print('Invalid Student ID')

        elif choice == 4:
            print('Thank You..')
            break
        else:
            print('Invalid choice.')

user()