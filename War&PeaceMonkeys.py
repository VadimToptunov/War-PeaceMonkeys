# author == "Vadim Toptunov"
# -*- coding: utf-8 -*-

import argparse #will be used later
import random
import string


def lowercase():
	lower = ''.join(random.choice(string.ascii_lowercase) for x in range (8, 1024))
	return lower


def uppercase():
	upper = ''.join(random.choice(string.ascii_uppercase) for x in range(8, 1024))
	return upper


def digits():
	digs = ''.join(random.choice(string.digits) for x in range(8, 1024))
	return digs


def wildcards():
	wild = ''.join(random.choice(string.punctuation) for x in range(8, 1024))
	return wild


def result_function():
	result = ''.join(random.choice(wildcards() + upppercase() + lowercase() + digits()) for x in range(8, 16))
	print "Your password is: " + result

if __name__ == "__main__":
	result_function()
