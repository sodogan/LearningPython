# Use keyword-only arguments to help ensure code clarity
# Asterisk lets us separate positional arguments from keyword arguments, thus making them keyword-only arguments
def myFunction(arg1, arg2, *, suppressExceptions=False):
    print("arg1={}, arg2={}, suppressExceptions={}".format(arg1, arg2, suppressExceptions))


def main():
    # Try to call the function without the keyword
    # myFunction(1, 2, True) ERROR, we used asterik * to force separate position arguments from keyword-only arguments
    myFunction(1, 2)
    myFunction(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()
