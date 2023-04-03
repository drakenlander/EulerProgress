'''

Longest Collatz Sequence
Problem 14

The following iterative sequence is defined for the set of positive
integers:

n → n / 2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.

'''

def collatzSequence(n, d):
	sz = 0; # sequence length
	og = n;

	while n != 1:
		if n < og: # check if previous sequence found
			d[og] = d[n] + sz; # sz = sz + previous sequence sz

			break;

		if n % 2 == 0:
			n = n / 2;
			sz = sz + 1;
		else:
			n = (3 * n + 1) / 2;
			sz = sz + 2;

	return sz;


d = {n: 0 for n in range(1, 1000001)};
d[2] = 2;

for i in range(1, 1000001):
	collatzSequence(i, d);

print(max(d.values()));
