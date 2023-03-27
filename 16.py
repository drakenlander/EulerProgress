def sumDigits(n):
	s = 0;

	for i in str(n):
		s = s + int(i);

	return(s);

	
x = 2 ** 1000;

print(x);
print(sumDigits(x));