#!/usr/bin/env python

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''

user_input = input()

binnum = [i for i in user_input.split(",")]

value = []
for p in binnum:
    bp = int(p,2)
    if bp % 5 == 0:
        value.append(bp)

print("".join(value))
        

