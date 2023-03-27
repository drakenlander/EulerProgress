from math import factorial;

def sumDigits(n):
	s = 0;

	for i in str(n):
		s = s + int(i);

	return(s);


prod = factorial(100);

print(prod);
print(sumDigits(prod));