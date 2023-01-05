'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class MyString:

    def __init_(self):
        self.s = ""

    def getString(self):
        self.s = input("Please enter a string: ")

    def printString(self):
        print(self.s.upper())

    

printstring = MyString()
printstring.getString()
printstring.printString()


