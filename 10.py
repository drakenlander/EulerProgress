'''

Summation of Primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def sieveOfErathostenes(n):
	primes = [True for i in range(n + 1)];
	p = 2;
	s = 0; # store sum of all primes

	while p ** 2 <= n: # repeat until sqrt of n
		if primes[p] == True: # if element is prime...
			for i in range(p ** 2, n + 1, p): # access all multiples
				primes[i] = False; # and remove them
				
		p = p + 1;

	for i in range(2, len(primes)):
		if primes[i]:
			s = s + i;

	return(s);


n = 2000000;
res = sieveOfErathostenes(n);

print(res);
