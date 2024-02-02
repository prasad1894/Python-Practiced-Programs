sum = 0
N = int(input("Enter Number: "))
a = 2
for i in range(1, N+1):
    if(i%2 == 0):
        sum = -a
    else:
        sum = a
    print("Sum of Series: ", sum)
    a *= 3