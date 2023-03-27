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