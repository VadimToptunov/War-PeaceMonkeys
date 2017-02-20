import random
import string


def lowercase():
	lower = ''.join(random.choice(string.ascii_lowercase) for x in range (8, 254))
	return lower


def uppercase():
	upper = ''.join(random.choice(string.ascii_uppercase) for x in range(8, 254))
	return upper


def digits():
	digs = ''.join(random.choice(string.digits) for x in range(8, 254))
	return digs


def wildcards():
	wild = ''.join(random.choice(string.punctuation) for x in range(8, 254))
	return wild


def result_function():
	low = lowercase()
	up = uppercase()
	digs = digits()
	wild = wildcards()
	result = ''.join(random.choice(wild + up + low + digs) for x in range(8, 16))
	print "Result: " + result

if __name__ == "__main__":
	result_function()