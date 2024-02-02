n = 508
temp = n
count = 0
while(temp!=0):
    d = temp % 10
    if(d == 0):
        count += 1
    temp = temp//10
if(count>0):
    print("Duck Number")
else:
    print("Not a Duck Number")