def isPalindrome(n):
	t = n;
	r = 0;

	while t != 0:
		r = r * 10 + t % 10; # takes last digit of t and backloads it into r
		t = (t - t % 10) / 10; # removes rightmost digit from t
	if n == r:
		return True;
	return False;


pos = [] # list of all palindromes

for i in range(999, 100, -1):
	for j in range(999, 100, -1):
		prod = i * j;
		if isPalindrome(prod):
			print(prod);
			pos.append(prod);
			
print(max(pos));