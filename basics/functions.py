# Functions are defined with a 'def' keyword:
def func1():
    # Function body is indented
    print("I am a function")


func1()
print(func1())  # None - function doesn't return anything, thus Python automatically assigns 'None' as result
print(func1)  # <function func1 at 0x03B03F60>


def square(x):
    return x * x


print('2 squared is ' + str(square(2)))


# Function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result *= num
    return result


print('2 in power 1 is ' + str(power(2)))
print('2 in power 2 is ' + str(power(2, 2)))
print('2 in power 3 is ' + str(power(2, 3)))
print('2 in power 8 is ' + str(power(2, 8)))

print('3 in power 2 is ' + str(power(x=2, num=3)))


# Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


print(multi_add(1)) 
print(multi_add(1, 2))
print(multi_add(1, 2, 3))
print(multi_add(1, 2, 4, 5, 6, 7, 8, 9))
