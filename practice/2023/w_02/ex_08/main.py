#!/usr/bin/env python

'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
user_input = input("Please enter a numbers comma separated: ").split(",")

sq_odd = []
for num in user_input:
    if int(num) % 2 != 0:
        sq_odd.append(int(num)*int(num))

sq_odd1 = [ x for x in user_input if int(x) % 2 !=0 ]
print(sq_odd)
print(sq_odd1)
