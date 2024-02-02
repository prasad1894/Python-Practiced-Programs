n = 5
p=65
for i in range(n):
    for j in range(n):
        if(j == 0 or i == n-1 or i == j):
            print(chr(p), end=' ')
        else:
            print(' ', end=' ')
        p += 1
    print()