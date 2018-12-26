import collections


def main():
    p = (10, 20)
    print(p)

    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(x=30, y=40)
    p3 = Point(y=100, x=50)
    print(p1)  # Point(x=10, y=20)
    print(p2)  # Point(x=30, y=40)
    print(p3)  # Point(x=50, y=100)

    print(p1.x)  # 10
    print(p2.y)  # 40

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1) # Point(x=100, y=20)


if __name__ == "__main__":
    main()
