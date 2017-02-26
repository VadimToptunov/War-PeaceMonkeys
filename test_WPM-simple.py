import random
import re
import string


def lowercase():
    # Create a random lowercase letters string
    lower = ''.join(random.choice(string.ascii_lowercase) for x in range (8, 1024))
    return lower


def test_lowercase():
    low = lowercase()
    test_result = low.islower()
    if test_result:
        print "OK!"
    else:
        print "Test failed!"


def uppercase():
    # Create a random uppercase letters string
    upper = ''.join(random.choice(string.ascii_uppercase) for x in range(8, 1024))
    return upper


def test_uppercase():
    upper = uppercase()
    test_result = upper.isupper()
    if test_result:
        print "OK!"
    else:
        print "Test failed!"


def digits():
    # Create a random digits string
    digs = ''.join(random.choice(string.digits) for x in range(8, 1024))
    return digs


def test_digits():
    digit = digits()
    test_result = digit.isdigit()
    if test_result:
        print "OK!"
    else:
        print "Test failed!"


def wildcards():
    # Create a random wildcards string
    wild = ''.join(random.choice(string.punctuation) for x in range(8, 1024))
    return wild


def test_wildcards():
    wld = wildcards()
    test_result = wld.isalnum()
    if not test_result:
        print "OK!"
    else:
        print "Test failed! "


#def result_function():
    # Create a complicated password containing uppercase, lowercase letters, wildcards and digits.
#    password = ''.join(random.choice(wildcards() + uppercase() + lowercase() + digits()) for x in range(8, 16))
#    return password


#def consecutive_check():
#    password = result_function()
#    pwd = str(password)
#    if not re.search(r"(.)\1\1", pwd):
#        print "Your password is: " + pwd
#    else:
#        new_pwd = result_function()
#        print "Your password: " + new_pwd


def test():
    test_lowercase()
    test_uppercase()
    test_digits()
    test_wildcards()
    #test_result_function()

if __name__ == "__main__":
    #consecutive_check()
    test()
