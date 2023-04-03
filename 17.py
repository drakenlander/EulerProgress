'''

Number Letter Counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when
writing out numbers is in compliance with British usage.

'''

def uLetterCount(n): # units and hundreds
	a = str(n);
	s  = 0;

	if a != "0":
		if a == "1" or a == "2" or a == "6":
			s = s + 3;
		elif a == "4" or a == "5" or a == "9":
			s = s + 4;
		else:
			s = s + 5;

	return s;


def tLetterCount(n): # teens
	a = str(n);
	s = 0;

	if a == "11" or a == "12":
		s = s + 6;
	elif a == "15" or a == "16":
		s =  s + 7;
	elif a == "13" or a == "14" or a == "18"  or a == "19":
		s = s  + 8;
	elif a == "17":
		s = s + 9;
	else:
		s = s + 3;

	return s;


def dLetterCount(n): # tens
	a = str(n);
	s = 0;

	if a == "2" or a == "3" or a == "8" or a == "9":
		s = s + 6;
	elif a == "4" or a == "5" or a == "6":
		s = s + 5;
	elif a == "7":
		s = s + 7;
	else:
		s = 0;

	return s;


s = 0;

for i in range(1, 10): # first 9
	s = s + uLetterCount(i);

for i in range(10, 20): # from 10 to 19
	s = s + tLetterCount(i);

for i in range(20, 100): # from 20 to 99
	s = s + dLetterCount(int(i / 10)) + uLetterCount(i % 10);

s = s * 10; # pattern repeats 10 times from 1 to 1000

for i in range(1, 10):
	s = s + ((uLetterCount(i) + 7) * 100); # every "'x'hundred"

s = s + (3 * 99) * 9; # every "and"
s = s + 11; # "onethousand"

print(s);
