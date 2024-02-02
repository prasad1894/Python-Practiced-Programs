n = 123
temp = n
sum = 0
prod = 1
while(temp!=0):
    d = temp % 10
    sum = sum + d
    prod = prod * d
    temp = temp // 10
if(sum == prod):
    print("Spy Number")
else:
    print("Not a Spy Number")