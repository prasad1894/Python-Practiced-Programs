sum = 0
x = int(input("Enter Number: "))
N = int(input("Enter Number: "))
a = 2
b = 10
for i in range(1, N+1):
    sum = sum + (x+a)/b
    a += 2
    b *= 3
    print("Sum of Series:", sum)