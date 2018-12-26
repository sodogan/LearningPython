def main():
    x = 0

    print("while loop")
    while x < 5:
        print(x)
        x += 1

    print("for loop")
    # let 'for' loop over a range of items (take it's items)
    for x in range(5, 10):
        print(x)
    # 'for' loops in Python are iterators

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
    # If you steel need counter:
    for i, d in enumerate(days):
        # destructuring tuple
        print(str(i) + ") " + d)

    for x in range(5, 10):
        if (x == 7): break
        print(x)
    # 5, 6

    for x in range(5, 10):
        if x % 2 == 0:
            # skip чётные numbers
            continue
        print(x)
    # 5, 7, 9


if __name__ == "__main__":
    main()
