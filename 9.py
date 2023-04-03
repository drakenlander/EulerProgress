'''

Special Pythagorean Triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.

Find the product abc.

'''

ppt = [];
n = 1;
sz = 1000;

for i in range(sz):
	ppt.append([]);
	m = n + 1;

	for j in range(sz):
		ppt[i].append([]);
		ppt[i][j].append(m ** 2 - n ** 2);
		ppt[i][j].append(2 * m * n);
		ppt[i][j].append(m ** 2 + n ** 2);
		m =  m + 1;

	n = n + 1;

for i in range(sz):
	for j  in range(sz):
		if ppt[i][j][0] + ppt[i][j][1] + ppt[i][j][2] == 1000:
			print(ppt[i][j]);
