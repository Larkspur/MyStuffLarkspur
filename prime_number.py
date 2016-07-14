def check_if_prime(number):
    factors = [number]
    for value in range(1, number):
        if number % value == 0:
            factors.append(value)
    if factors == [number, 1]:
        return True
    else:
        return False
def list_factors(number):
    factors = []
    for value in range(1, number):
        if number % value == 0:
            factors.append(value)
    factors.append(number)
    return factors
def prime_factorization(number):
    smaller_primes = []
    for value in range(2, number + 1):
        if check_if_prime(value) == True:
            smaller_primes.append(value)
    for value in smaller_primes:
        
        while number % value == 0:
            
