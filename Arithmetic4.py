import math as m
sum = 0
x = int(input("Enter Number: "))
N = int(input("Enter Number: "))
k = 5
a1 = 1
a2 = 2
for i in range(1, N+1):
    sum = sum + (x+k**2)/(a1+m.factorial(a2))
    k *= 5
    a1 += 1
    a2 += 1
    print("Sum of Series:", sum)