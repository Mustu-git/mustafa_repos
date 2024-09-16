
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to return a list of prime numbers from the input list
def filter_primes(numbers):
    primes = [num for num in numbers if is_prime(num)]
    return primes

# Example usage
numbers = [10, 3, 7, 11, 4, 13, 15, 20]
prime_numbers = filter_primes(numbers)
print("Prime numbers:", prime_numbers)

