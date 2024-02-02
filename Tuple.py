Student = ("Prasad", 21, "Male")
print(Student.count("Prasad"))
print(Student.index("Male"))
for i in Student:
    print(i)
if "Prasad" in Student:
    print("Prasad is Here!")