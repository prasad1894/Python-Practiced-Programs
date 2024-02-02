import csv
f1 = open('student1.csv', 'w')
w1 = csv.writer(f1, delimiter= ":")
w1.writerow(['RollNo', 'Name', 'Marks'])
w1.writerow(['01', 'Srinu', '90'])
w1.writerow(['02', 'Naveen', '80'])
f1.close()