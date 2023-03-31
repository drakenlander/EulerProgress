'''

Large Sum
Problem 13

Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.

'''

f = open("numbers.txt", "r");

A = [];
s = 0;

for x in f:
	A.append(int(x));

for i in A:
	s = s + i;

print(str(s)[: 10]);
