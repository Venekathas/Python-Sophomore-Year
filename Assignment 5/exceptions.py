# Exception handling examples
# Adopted from www.python-course.eu


# Repeatedly prompt the user for input until they enter an integer
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        # if the previous statement executes without error, loop terminates
        break
    except ValueError:
        print("No valid integer! Please try again ...")

print("Great, you successfully entered an integer!\n")



# Handle multiple exceptions

f = None
print("Attempting to open 'integers.txt' and output its contents")
try:
    f = open('integers.txt')
    for s in f:
        i = int(s.strip())
        print(i)
except IOError as e:
    print(e)
except ValueError:
    print("No valid integer in line.")
finally:
    # close the file if it was open successfully
    if f is not None:
        f.close()


