Student1 = {"Ram", "Venu", "Dinesh"}
Student2 = {"Girish", "Harsha", "Bharath"}
Student1.add("Aravind")
#Student1.update(Student2)
Students = Student1.union(Student2)
#Students = Student1.difference(Student2)
for i in Students:
    print(i)