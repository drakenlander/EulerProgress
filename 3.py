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
			print(i, n / i);
			n = n / i; # lower limit
	i = i + 1;
	
print(i, n);