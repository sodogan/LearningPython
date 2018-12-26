import collections


def main():
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

    # count fruits using simple dictionary
    fruitCounter = {}

    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    for (k, v) in fruitCounter.items():
        print("{} - {}".format(k, v))

        # count fruits using simple dictionary
        fruitCounter = {}

    # do the same with defaultdict
    # defaultdict provides default value the first time value is accessed
    fruitCounter = collections.defaultdict(int)
    # fruitCounter = collections.defaultdict(lambda: 100)
    for fruit in fruits:
        # no need to check whether keys exists or not
        fruitCounter[fruit] += 1

    for (k, v) in fruitCounter.items():
        print("{} - {}".format(k, v))


if __name__ == "__main__":
    main()
