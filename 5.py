'''

Smallest Multiple
Problem 5

2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

'''

def isDivisible(n):
	divisors = [18, 16, 14]; # other divisibilities are given

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
		n = n + f; # multiple of f to be divisible by other divisors
