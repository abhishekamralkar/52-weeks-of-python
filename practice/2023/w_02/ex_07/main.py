#!/usr/bin/env python

'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
upper_count = 0
lower_count = 0
user_input= input()
s = [x for x in user_input.strip()]
for i in s:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1

print(f"Upper Case: {upper_count}")
print(f"Lower Case: {lower_count}")

        
