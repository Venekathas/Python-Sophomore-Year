

'''This function takes a string and returns it in reverse order.
    @param string The string to be reversed.
    @return string The string reversed.
'''
def reverse_string(string):
    if len(string)==1:
        return(string)
    else:
        
        return(reverse_string(string[1:])+ string[0])

'''This function prints a string starting with its last value, and reprinting
    the string adding the next part until its full.
    @param string The string to print.
'''
def rec_string(string):
    if len(string) == 0:
        print("*")
    else:
        rec_string(string[1:])
        print(string)

'''This main function tests the reverse_string and rec_string functions.
    It gets a string from the user, sends it to rec_string for printing
    and then to reverse string to get the reverse of the string to print
    from within the main funciton.
    @param string The string to send to other functions.
'''
def main():
    string=(input("Give me a string!: "))
    rec_string(string)
    print("\nNow let me reverse the string!\n")
    string=reverse_string(string)
    print(string)

if __name__ == "__main__":
    main()
    
                         
