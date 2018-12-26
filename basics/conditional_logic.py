def main():
    x, y = 10, 100
    if x < y:
        st = "x is less than y"
    elif x > y:
        st = "x is bigger than y"
    else:
        st = "x is equalt to y"

    print(st)
    st2 = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(st2)

    # Python doesn't have 'switch' statement


if __name__ == "__main__":
    main()
