n = int(input("Enter any Number: "))
sum = 0
a = 1
for i in range(1, n+1):
    sum = sum + a
    a += 1
    print("Sum of Series: ", sum)