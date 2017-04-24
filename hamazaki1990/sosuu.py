N = 1000
for n in range(2, N+1):
    for a in range(2, n):
        if n % a == 0:
            break
        else:
            print(n)
