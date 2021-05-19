#In order to access the Python library, we need to import the package in our Python script.
# Tips: https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9

import random
import string

#test with greeting
print('hello, Welcome to Password generator!')
length = int(input('\n Enter the length of your password'))

#define variable
letter = string.ascii_letters
upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
symbols = string.punctuation

all = upper + lower + num + symbols
temp = random.sample(all, length)
password = "".join(temp)
print (password)

#or shorter way to write below
all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all, length))
print (password)
