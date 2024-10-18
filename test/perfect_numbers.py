def primez(n):
    listo = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            listo.append(i)
    if sum(listo) == n:
        return True


def primes(n):
    listo = []
    for i in range(1, n):
        if primez(i):
            listo.append(i)
    return listo


print(primes(1000000))
