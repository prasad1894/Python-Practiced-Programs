n = 153
temp = n
sum = 0
while(temp!=0):
    d = temp % 10
    sum = sum + d ** 3
    temp = temp // 10
if(sum == n):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")