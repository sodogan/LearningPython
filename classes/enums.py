from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # repeating values are allowed if unique is not specified @unique
    # RED_DELICIOUS = 1
    # If you don't care about values, use 'auto' function
    PEAR = auto()


def main():
    apple = Fruit.APPLE
    print(apple)
    print(type(apple))
    print(repr(apple))

    print(apple.name)
    print(apple.value)

    banana = Fruit(2)
    print(banana)

    print(Fruit.PEAR.value)


if __name__ == "__main__":
    main()
