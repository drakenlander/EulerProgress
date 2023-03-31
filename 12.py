'''

Highly Divisible Triangular Number
Problem 12

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five
hundred divisors?

'''

from collections import Counter;

def findDivs(n):
	factors = []; # store prime factors
	i = 2; # first possible divisor to check
	res = 1;

	while i <= n:
		if n % i == 0:
			n = n / i; # lower limit
			factors.append(i);
		else:
			i = i + 1;

	dictDivForm = {i:factors.count(i) for i in factors}; # exponents

	for v in dictDivForm.values():
		res = res * (v + 1); # total divisors

	print(dictDivForm);
	print(res);

	return(res);


s = 0;
c = 0;

while True:
	s = s + c;
	print(s);

	finalRes = findDivs(s);

	if finalRes > 500:
		exit();

	c = c + 1;
