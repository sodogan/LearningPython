def filterFunc(x):
    if x % 2 == 0:
        # value is even, remove it
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def toGrade(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 65 <= x < 70:
        return "D"
    else:
        return "F"


def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    # return false to remove item from the resulting sequence
    odds = list(filter(filterFunc, nums))
    print(odds)

    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # use map to create a new sequence of values
    squares = list(map(lambda x: x ** 2, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(grades)
    print(letters)


if __name__ == "__main__":
    main()