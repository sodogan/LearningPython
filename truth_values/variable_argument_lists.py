# To define a variable number of arguments, place asterisk (*) before variable name
# Type will be 'Tuple'
def addition(*numbers):
    print("addition( {} )".format(numbers))
    print(sum(numbers))


def main():
    addition()
    addition(1)
    addition(1, 2, 3)
    addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


if __name__ == "__main__":
    main()
