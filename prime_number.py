def check_if_prime(number):
    factors = [number]
    for value in range(1, (number + 1) / 2 + 1):
        if number % value == 0:
            factors.append(value)
    if factors == [number, 1]:
        return True
    else:
        return False

def list_factors(number):
    factors = []
    for value in range(1, (number + 1) / 2 + 1):
        if number % value == 0:
            factors.append(value)
    factors.append(number)
    final = []
    for factor in factors:
        final.append(str(factor))
    return "Factors: " + ", ".join(final)

def prime_factorization(number):
	if check_if_prime(number) == True:
		return number
	else:
    	prime_factors = []
    	for value in range(2, (number + 1) / 2 + 1)
        	if check_if_prime(value) == True:
            	while number % value == 0:
            		prime_factors.append(value)
            		number = number / value
    	return prime_factors
