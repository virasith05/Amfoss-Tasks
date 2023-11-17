t = int(input())

for j in range(t):
    n = int(input())
    largest_prime_factor = 0

    while n % 2 == 0:
        largest_prime_factor = 2
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime_factor = i
            n //= i

    if n > 1:
        largest_prime_factor = n

    print(largest_prime_factor)

