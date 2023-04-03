'''

Largest Palindrome Product
Problem 4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.

'''

def isPalindrome(n):
	t = n;
	r = 0;

	while t != 0:
		r = r * 10 + t % 10; # insertion of last digit of t into r
		t = (t - t % 10) / 10; # removes rightmost digit from t

	if n == r:
		return True;

	return False;


pos = [] # list of all palindromes

for i in range(999, 100, -1):
	for j in range(999, 100, -1):
		prod = i * j;

		if isPalindrome(prod):
			pos.append(prod);

print(max(pos));
