#!/usr/bin/python

'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def main():
    start = 2000
    end = 3201
    print(find_number(start, end))

def find_number(start, end):
    num_list = []
    for number in range(start, end):
        if number % 7 == 0 and number % 5 != 0:
            num_list.append(number)
    return (''.join(num_list))

#if __name__ == "__main__":
main()

