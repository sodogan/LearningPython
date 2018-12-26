# declare a variable and print it
f = 0
print(f)

# re-declare the variable
f = 'abc'
print(f)

#  ERROR: variables of different types cannot be combined
# print("This is a string" + 123)
# OK: int is converted to string
print("This is a string" + str(123))


# Global vs. local variables in functions
def someFunction():
    f = "def"
    print("someFunction: " + f)


someFunction()
print(f)  # still "abc", unchanged, since f is not gloal


def someFunction2():
    # define f as global variable
    global f
    f = "def"
    print("someFunction2: " + f)


someFunction2()
print(f)

# Delete definition of the variable
del f
# Error: NameError: name 'f' is not defined
print(f)
