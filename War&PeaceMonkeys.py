# author == "Vadim Toptunov"
# -*- coding: utf-8 -*-

import argparse
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
    result = ''.join(random.choice(wildcards() + uppercase() + lowercase() + digits()) for x in range(8, 16))
    return result

def main():
    argparser = argparse.ArgumentParser()
    group = argparser.add_mutually_exclusive_group()
    group.add_argument("-l", help="Use the option to set lowercase letters in your password", action="store_true")
    group.add_argument("-u", help="Use the option to set uppercase in your password", action="store_true")
    group.add_argument("-d", help="Use the option to set digits in your password", action="store_true")
    group.add_argument("-w", help="Use the option to set wildcards in your password", action="store_true")
    group.add_argument("-lu", help = "Use the option if you want a password only with uppercase and lowercase letters", \
                       action="store_true")
    group.add_argument("-lud", help= "Add lowercase, uppercase letters and digits to your password", action="store_true")
    group.add_argument("-ludw", help="Add lowercase, uppercase letters, digits and wilcards to your password",
                       action="store_true")
    group.add_argument("-ld", help="Add only lowercase letters and digits to your password.", action="store_true")
    group.add_argument("-ud", help="Add only uppercase letters and digits to your password.", action="store_true")
    group.add_argument("-lw", help="Add only lowercase letters and wildcards in your password.", action="store_true")
    group.add_argument("-uw", help="Add only uppercase letters and wildcards in your password.", action="store_true")
    group.add_argument("-dw", help="Add only lowercase digits and wildcards in your password.", action="store_true")
    args = argparser.parse_args()

    if args.l:
        res = ''.join(random.choice (lowercase()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.u:
        res = ''.join(random.choice(uppercase()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.d:
        res = ''.join(random.choice(digits()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.w:
        res = ''.join(random.choice(wildcards()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.lu:
        res = ''.join(random.choice(lowercase() + uppercase()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.ludw:
        res = result_function()
        print "Your password is: " + res
    elif args.lud:
        res = ''.join(random.choice(lowercase() + uppercase() + digits()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.ld:
        res = ''.join(random.choice(digits() + lowercase()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.ud:
        res = ''.join(random.choice(uppercase() + digits()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.lw:
        res = ''.join(random.choice(lowercase() + wildcards()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.uw:
        res = ''.join(random.choice(uppercase() + wildcards()) for x in range(8, 16))
        print "Your password is: " + res
    elif args.dw:
        res = ''.join(random.choice(digits() + wildcards()) for x in range(8, 16))
        print "Your password is: " + res
    else:
        print "No option is set!"


if __name__ == "__main__":
    main()
