#!/usr/bin/env python

'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

letters = ''
digits = ''

s = input()

words = [word for word in s.split(" ")]

for word in words:
    #print(word)
    for i in word:
        if i.isalpha():
            letters += i
        elif i.isalnum():
            digits += i

print(f"Letters {len(letters)}")
print(f"Digits {len(digits)}")
