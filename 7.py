from math import log;

def isPrime(n):
	for i in range(2, n): # possible divisors
		if n % i == 0: # divisible; not prime
			return False;
	return True;


n = 1; # first prime is 2; purpose: to add 2 and skip even numbers
w = 10001;
c = 0;

while c != w:
	if isPrime(n):
		print(n);
		c = c + 1;

	n = n + 2;

print(c);

'''
# TODOTODOTODOTODOTODOTODOTODOTODOTODO

lowerBound = w * log(w);
upperBound = 1.5 * (w * log(w));
print(lowerBound, upperBound);

# TODOTODOTODOTODOTODOTODOTODOTODOTODO
'''