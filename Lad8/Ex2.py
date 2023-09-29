class Person():
    def __init__(self):
        #list of attributes
        self.name = ""
        self.age = 0
        self.gender = ""

    def info(self):
        print(f'Name:{self.name} Age: {self.age} Gender: {self.gender}')

class Employee(Person): #Employee inherited from person
    def __init__(self):
        self.emp_id = ""
        self.position = ""

    # def info(self):
    #     print(f'Name:{self.name} '
    #           f'Age: {self.age} '
    #           f'Gender: {self.gender}'
    #           f'EMP_ID: {self.emp_id}'
    #           f'Position: {self.position}')

#create object
p1 = Person()
p1.name ="Anutta Thongdet"
p1.age = 21
p1.gender = "Male"

emp1 = Employee()
emp1.name = "Nattakarn Film"
emp1.age = 21
emp1.gender = "Male"
emp1.emp_id = "EMPMT01"
emp1.position = "Lecturer"

p1.info()
emp1.info()

lst = [p1,emp1]
for obj in lst:
    print(obj.__class__.__name__, end=" " )
    obj.info()


class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.studentID = 0
        self.major = ""
        self.university = ""

    # def info(self):
    #     print(f'Name: {self.name} '
    #           f'Age: {self.age} '
    #           f'Gender: {self.gender}'
    #           f'StudentID: {self.studentID}'
    #           f'Major: {self.major}'
    #           f'University: {self.university}')

std1 = Student()
std1.name = "Anutta Thongdet"
std1.age = 21
std1.gender = "Woman"
std1.studentID = 364411760003
std1.major = "MIT431"
std1.university = "RUTS"

p1.info()
emp1.info()
std1.info()

lst = [p1,emp1,std1]
for obj in lst:
    print(obj.__class__.__name__, end=" ")
    obj.info()
