#!/usr/bin/env python

'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

user_input = input("Please enter a comma separated list of strings: ").split(",")
print(user_input)

print(type(user_input))

print(sorted(user_input))

print(user_input.sort())

