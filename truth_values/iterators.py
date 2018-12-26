def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jey", "Ven", "Sam"]

    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # continue loop
    for day in i:
        print(day)

    # Iterate over a file
    with open("testfile.txt") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    for m in days:
        print(m)

    for m in range(len(days)):
        print(m + 1, days[m])

    # Same as above, but easier to read
    for i, m in enumerate(days, start=1):
        print(i, m)

    # Use zip to combine sequences in a single iterator
    for m in zip(days, daysFr):
        # m is a Tuple
        print(m)

    # destructure tuple:
    for day, dayFr in zip(days, daysFr):
        # m is a Tuple
        print(day, dayFr)

    for i, m in enumerate(zip(days, daysFr)):
        print(i, m[0], m[1])


if __name__ == "__main__":
    main()
