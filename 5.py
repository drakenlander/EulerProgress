def isDivisible(n):
	divisors = [18, 16, 14]; # other divisibilities are given by prior calculation

	for i in divisors:
		if n % i != 0:
			return False;
	return True;


f = 19399380; # first number divisible by 20 and all primes below 20
n = f;

while True:
	print(n);
	
	if isDivisible(n):
		exit();
	else:
		n = n + f; # first multiple of f to be divisible by other divisors