'''

Even Fibonacci Numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do
not exceed four million, find the sum of the even-valued terms.

'''

sum = 2; # first even fibonacci number
fibA = 1;
fibB = 2;

while (fibB < 4000000):
	fibTmp = fibB;
	fibB = fibA + fibB;
	fibA = fibTmp;

	if fibB % 2 == 0 and fibB < 4000000:
		print(sum);
		sum = sum + fibB;
		
print(sum);
