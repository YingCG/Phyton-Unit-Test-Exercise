#In order to access the Python library, we need to import the package in our Python script.

import random
import string

#test with greeting
print('hello, Welcome to Password generator!')

#Next, let’s ask the user for the length of the password.
length = int(input('\nEnter the length of password: '))

# to define the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine and store the data
all = lower + upper + num + symbols

#generate the password
temp = random.sample(all,length)
password = "".join(temp)

#https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9