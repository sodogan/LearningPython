class myClass():
    # self argument refers to the object itself. It's like 'this' keyword in Java
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)


# Extend class
class anotherClass(myClass):
    def method1(self):
        # call parent class's method1
        myClass.method1(self)
        print("anotherClass method1")

    # def method2(self, someString):
    #     print("anotherClass method2 " + someString)


def main():
    myObject = myClass()
    print(myObject)
    # We don't need to supply 'self' keyword. It is handled by Python
    myObject.method1()
    myObject.method2("Hello, World!")

    c2 = anotherClass()
    c2.method1()
    # use inherited method
    c2.method2("Called on c2")


if __name__ == "__main__":
    main()
