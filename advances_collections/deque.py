from collections import deque


def main():
    # double-ended queue, pronounced "deck"
    d = deque("abcdefg")
    print(d)

    d.appendleft("1")
    d.append("9")
    print(d)

    print("Item count:", str(len(d)))

    for e in d:
        print(e.upper(), end=",")

    d.popleft()
    print(d)
    d.pop()
    print(d)

    # rotate towards the end by 10 items
    d.rotate(3)
    print(d)
    d.rotate(-3)
    print(d)


if __name__ == "__main__":
    main()
