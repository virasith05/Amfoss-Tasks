t=input("Enter a number (n): ")

if t.isdigit():
    n=int(t)

    if n < 2:
        print("There are no prime numbers less than 2.")
    else:
        prime_numbers = []

        for num in range(2, n + 1):
            is_prime = True
            for divisor in range(2, int(num**0.5) + 1):
                if num % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

        print("Prime numbers up to", n, "are:", prime_numbers)
else:
    print("Invalid input. Please enter a valid number")
