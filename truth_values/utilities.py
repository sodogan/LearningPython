def main():
    list1 = [1, 2, 3, 0, 5, 6]
    # any will return true if any of the sequence values are true
    print(any(list1))
    # all will return true if all of the sequence values are true
    print(all(list1))

    print("min:", min(list1))
    print("max:", max(list1))
    print("sum:", sum(list1))


if __name__ == "__main__":
    main()
