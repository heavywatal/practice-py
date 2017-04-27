N = 1000
for n in range(2, N+1):
    for a in range(2, n):
        if n % a == 0:
            break
    else:
        print(n)


def is_prime(x):
    for a in range(2, x):
        if x % a == 0:
            return "false"


for n in range(2, N+1):
    if is_prime(n) == "false":
        break
else:
    print(n)
