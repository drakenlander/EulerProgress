sumOfSquares = 0;

for i in range(101):
	sumOfSquares = sumOfSquares + i ** 2;

print(sumOfSquares);

squareofSum = 0;

for i in range(101):
	squareofSum = squareofSum + i;

squareofSum = squareofSum ** 2;
print(squareofSum);

res = squareofSum - sumOfSquares;
print(res);