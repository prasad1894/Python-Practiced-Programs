class Student:
    def __init__(self, sname, rollno, age, gender, branch):
        self.sname = sname
        self.rollno = rollno
        self.age = age
        self.gender = gender
        self.branch = branch
    #def display(self):
        print("Name: ", self.sname)
        print("RollNo: ", self.rollno)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Branch: ", self.branch)
        print("_________________________________")
S1 = Student("Divya", 1, 22, "Female", "Civil")
S2 = Student("Siva", 12, 24, "Male", "Mech")
S3 = Student("Ganesh", 17, 19, "Male", "EEE")
S4 = Student("Anjali", 7, 25, "Female", "CSE")

#S1.display()
#S2.display()
#S3.display()
#S4.display()