sum = 0;

for i in range(1001):
	if i % 3 == 0 or i % 5 == 0:
		print(sum);
		sum = sum + i;
		
print(sum);