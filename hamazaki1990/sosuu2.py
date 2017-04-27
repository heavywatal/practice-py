def is_prime(x):
    for a in range(2, x):
        if x % a == 0:
<<<<<<< HEAD
            break
    else:
        return "true"
=======
            return False
    else:
        return True
>>>>>>> a13e7262e49f2ace1afee62e5a3fbac4efc87333


N = 1000
for n in range(2, N+1):
<<<<<<< HEAD
    if is_prime(n) == "true":
=======
    if is_prime(n):
>>>>>>> a13e7262e49f2ace1afee62e5a3fbac4efc87333
        print(n)
