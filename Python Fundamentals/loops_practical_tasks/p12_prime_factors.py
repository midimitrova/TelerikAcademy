
n = int(input())
def prime_factorization(n):
    prime_factors = []
    while (n % 2 == 0):
        n = n / 2
        prime_factors.append(2)
    for i in range(3, int(n**0.5 + 1), 2):
        while (n % i == 0):
            n = n / i
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors
print('\n'.join(map(str, prime_factorization(n))))
