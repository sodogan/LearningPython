"""This is documentation of docstrings.py module
"""


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything, just prints.

    :param arg1: The first argument. Whatever you feel like passing.
    :param arg2: Second argument. Defaults to None.
    :return: Sum of arg1 and arg2
    """
    print(arg1, arg2)
    return arg1 + arg2


# More info about docstrings: https://www.python.org/dev/peps/pep-0257
def main():
    print(myFunction.__doc__)
    print(__doc__)


if __name__ == "__main__":
    main()
