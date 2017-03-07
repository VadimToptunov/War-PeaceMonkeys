# author == "Vadim Toptunov"
# -*- coding: utf-8 -*-

"""
The simple script generates secure passwords, which contain lowercase and uppercase letters, digits and wildcards. 
The passwords are also checked on 3 consecutive symbols in it. 

To run the script just create a python file with it and run:

Your@Comp:~$ python /home/your_directory/WPM-simple-script.py 

"""

import random
import re
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
        password = ''.join(random.choice(wildcards() + uppercase() + lowercase() + digits()) for x in range(8, 16))
        return password

def consecutive_check():
        password = result_function()
        pwd = str(password)
        if not re.search(r"(.)\1\1", pwd):
		print "Password is: " + pwd
        else:
                new_pwd = result_function()
                print "Password: " + new_pwd

		
def wh():
        qx = raw_input("How many passwords do you need? ")
        qx = int(qx)
	 direct = raw_input("Set your directory to create a new file" \
        " for passwords: ")
        date2day = datetime.date.today()
        dt = []
        dt.append(date2day)
        today = str(dt[0])
        filename = direct + "passwords-" + today + "-" + ".txt"

        f1 = open(filename, "a")
        while qx != 0:
                pwd = consecutive_check()
		f1.write(pwd + "\n\n")
                qx -= 1
        f1.close()
	print "Now you can see your passwords here: ", filename
		
		
if __name__ == "__main__":
	wh()
