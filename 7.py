'''

10001st Prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

'''

from math import log;

def sieveOfErathostenes(index, bound):
	primes = [True for i in range(bound + 1)];
	p = 2;
	c = 0; # count every prime

	while p ** 2 <= bound: # repeat until sqrt of bound
		if primes[p] == True: # if element is prime...
			for i in range(p ** 2, bound + 1, p): # access multiples
				primes[i] = False; # and remove them
				
		p = p + 1;

	for i in range(2, len(primes)):
		if primes[i] == True:
			c = c + 1;

		if c == index:
			return(i);


index = 10001;
bound = int(index * (log(index) + log(log(index))));

print(sieveOfErathostenes(index, bound));
