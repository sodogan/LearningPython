class Person:

    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # str(object), print(object), "{0}".format(object)
    def __str__(self):
        return "Person ({} {} is {})".format(self.fname, self.lname, self.age)

    # Print detailed and useful data
    # Often used for debugging
    # repr(object)
    def __repr__(self):
        return "<Person Class - fname:{}, lname:{}, age:{}>".format(self.fname, self.lname, self.age)

    # format(object, format_spec)
    def __format__(self, format_spec):
        return "Fruit"

    # Convert object to bytes
    def __bytes__(self):
        val = "Person:{}:{}:{}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))

def main():
    cls1 = Person()
    print(repr(cls1))
    print(str(cls1))
    print(cls1)
    print("Formatted: {}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()
