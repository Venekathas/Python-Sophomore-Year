#Bradley Smith /  3/1/2017  /  Assignment 4:Palindrome
#Professor Amal Abdel Raouf  /  CSC 212

'''This program checks to see if a user submitted string is a palindrome or not.'''

import Stack

def Palindrome(alist):
    s= Stack.Stack()
    for x in alist:
        s.push(x)
    match = True
    string = ''
    for x in range(len(alist)):
        if s.peek() != alist[x] and match == True:
            match=False
        string = string + s.pop()
    print("String in reverse: " + string)
    return match

def main():
    string =input("Give me a word! I'll check to see if it's a palindrome!: ")
    alist = []
    for x in string:
        alist.append(x)
        
    match = Palindrome(alist)
    print("Original String:   " + string)
    if match == True:
        print("It is a palindrome!")
    else:
        print("It's not a palindrome.")

    x = "110"
    y = 110
    print(x)
    print(y)

if __name__== "__main__":
    main()

            
        
