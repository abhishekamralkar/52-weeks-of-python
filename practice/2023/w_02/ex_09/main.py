#!/usr/bin/env python

'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''


def total()
deposit = 0

while True:
    amount = input("Please enter a number: ")

    print(amount)
    if not amount:
        break
    values = amount.split(" ")
    if amount[0] == 'D':
        deposit += int(values[1])
    elif amount[0] == 'W':
        deposit -= int(values[1])

print(deposit)
        
    
