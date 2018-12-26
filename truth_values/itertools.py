import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    # starts from beginning
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    # params: start, step
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    # default accumulation function is addition
    acc = itertools.accumulate(vals, max)
    print(list(acc))

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals))) # drops values while testFunction returns True
    print(list(itertools.takewhile(testFunction, vals))) # takes values as long as testFunction returns True


if __name__ == "__main__":
    main()
