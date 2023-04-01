'''

Largest Prime Factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

'''

def isPrime(n):
	for i in range(2, n): # possible divisors
		if n % i == 0: # divisible; not prime
			return False;

	return True;


n = 600851475143;
i = 2;

while n != i:
	if isPrime(i):
		if n % i == 0:
			n = n / i; # lower limit
			
	i = i + 1;
	
print(i);
