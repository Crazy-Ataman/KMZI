import math

def gcd(a, b):
    # base case
    if b == 0:
        return a
    # recursive case
    return gcd(b, a % b)

def gcd_of_three(a, b, c):
    gcd_ab = gcd(a, b)
    return gcd(gcd_ab, c)


def is_prime(num):
    """Function to check if a number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def search_primes(start, end):
    """Function to search for prime numbers in a given interval"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print(f"GCD of 12 and 18: {gcd(12, 18)}")
print(f"GCD of 12, 77 and 299: {gcd_of_three(12, 77, 299)}")

print("Finding primes in interval [2,457]:")
primes = search_primes(2, 457)
print(primes)
print(f"The number of primes is {len(primes)}")
expected_count = 457 / math.log(457)
print(f"Actual number of primes in interval [2, 457]: {len(primes)}")
print(f"Expected number of primes in interval [2, 457]: {expected_count}")

print("Finding primes in interval [421,457]:")
primes = search_primes(421, 457)
print(primes)
print(f"The number of primes is {len(primes)}")
expected_count = 457 / math.log(457)
print(f"Actual number of primes in interval [2, 457]: {len(primes)}")
print(f"Expected number of primes in interval [421, 457]: {expected_count}")