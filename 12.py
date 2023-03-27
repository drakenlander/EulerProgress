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