n = 5
p = 1
for i in range(n):
    for j in range(n):
        if(j == 0 or j ==n-1):
            print(p, end=' ')
        else:
            print(' ', end=' ')
        p += 1
    print()