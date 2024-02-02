n = 24642
temp = n
sum = 0
while(temp!=0):
    d = temp % 10
    sum = sum * 10 + d
    temp = temp // 10
if(sum == n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")