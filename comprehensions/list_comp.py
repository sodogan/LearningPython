def main():
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # square even numbers and filter
    evenSquared = list(
        map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens)))
    print(evenSquared)

    # use comprehensions for the same operations
    evenSquared = [e ** 2 for e in evens]
    print(evenSquared)

    oddSquared = [e ** 2 for e in odds if 3 < e < 17]
    print(oddSquared)


if __name__ == "__main__":
    main()
