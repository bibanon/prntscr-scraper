#!/usr/bin/python3
# prntscr.com Imgur URL scraper
# base36.py
# Basic helper library for decimal to base36 conversion
# Written by Antonizoon for the Bibliotheca Anonoma Scripting Commission

def base36encode(number):
	if not isinstance(number, (int)):
		raise TypeError('number must be an integer')
	if number < 0:
		raise ValueError('number must be positive')

	alphabet, base36 = ['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', '']

	while number:
		number, i = divmod(number, 36)
		base36 = alphabet[i] + base36

	return base36 or alphabet[0]


def base36decode(b36_num):
	# take in base 36 string, whether uppercase or lowercase
	return int(b36_num.upper(), 36)

# convert an index to a prntscr id
# takes in an integer, then converts it to base36 with lowercase
# and padded to 6 places
def tobase36(num):
	return base36encode(num).lower().zfill(6)