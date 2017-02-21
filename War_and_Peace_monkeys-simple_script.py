# author == "Vadim Toptunov"
# -*- coding: utf-8 -*-

import random
import string


def lowercase():
	# Create a random lowercase letters string
	lower = ''.join(random.choice(string.ascii_lowercase) for x in range (8, 1024))
	return lower


def uppercase():
	# Create a random uppercase letters string
	upper = ''.join(random.choice(string.ascii_uppercase) for x in range(8, 1024))
	return upper


def digits():
	# Create a random digits string
	digs = ''.join(random.choice(string.digits) for x in range(8, 1024))
	return digs


def wildcards():
	# Create a random wildcards string
	wild = ''.join(random.choice(string.punctuation) for x in range(8, 1024))
	return wild

def result_function():
	# Create a complicated password containing uppercase, lowercase letters, wildcards and digits.
    result = ''.join(random.choice(wildcards() + uppercase() + lowercase() + digits()) for x in range(8, 16))
    print "Your password is: " + result


if __name__ == "__main__":
    result_function()
