def is_prime(x):
    for a in range(2, x):
        if x % a == 0:
            break
    else:
        return "true"


N = 1000
for n in range(2, N+1):
    if is_prime(n) == "true":
        print(n)
