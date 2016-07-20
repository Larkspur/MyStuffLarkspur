def check_if_prime(number):
	if number <= 1:
		return False
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
	prime_factors = []
	original = number
	if check_if_prime(number) == True:
		prime_factors.append(number)
	else:
		value = 2
		while value <= number:
			if check_if_prime(value) == True:
				while number % value == 0:
					prime_factors.append(value)
					number = number / value
			value += 1
	final = []
	for prime in prime_factors:
	    final.append(str(prime))
	return "Prime factorization of " + str(original) + ": " + \
	" x ".join(final)
