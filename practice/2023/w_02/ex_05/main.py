#!/usr/bin/env python

'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

even_list=[]
for num in range(1000, 1010):
   num = str(num)
   #rint(type(num))
   for i in num:
       if int(i) % 2 == 0:
           even_list.append(num)

print(even_list)
