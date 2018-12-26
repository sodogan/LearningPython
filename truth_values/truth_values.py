def main():
    # Any object is considered to be a boolean true or false
    # False and None evaluate to false
    # Numeric zero values: 0, 0.0, 0j
    # Decimal(0), Fraction(0, x)
    # Empty sequences/advances_collections: '', (), [], {}
    # Empty sets and ranges: set(), range(0)

    # Custom objects are considered true, unless defined otherwise by overriding _bool_ or __len__
    # class myClass:
    #     def __bool__(self):
    #         return False
    #
    #     def __len__(self):
    #         return 0

    if not 0:
        print("0 is evaluated to False")
    if not 0.0:
        print("0.0 is evaluated to False")
    if not []:
        print("[] is evaluated to False")


if __name__ == "__main__":
    main()
