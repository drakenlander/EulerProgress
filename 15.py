'''

Lattice Paths
Problem 15

Starting in the top left corner of a 2 × 2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the
bottom right corner.

How many such routes are there through a 20 ×  20 grid?

'''

from math import factorial;

def latticePaths(k, n):
	s = k + n;

	return(factorial(s) / (factorial(s - k) * factorial(k)));


print(latticePaths(20, 20));
