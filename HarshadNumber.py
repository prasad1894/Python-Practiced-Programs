n = 156
temp = n
sum = 0
while(temp!=0):
    d = temp % 10
    sum = sum + d
    temp = temp // 10
if(temp // sum == 0):
    print("Harshad or Niven Number")
else:
    print("Not a Harshad/Niven Number")