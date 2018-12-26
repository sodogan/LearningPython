import time
import datetime
from math import floor


def funcWithCallback(callback):
    time.sleep(3)
    if (callback):
        print("Calling callback")
        callback(floor(datetime.datetime.now().timestamp()))


def FahrenheitToCelsius(t):
    return (t - 32) * 5 / 9


def main():
    print("Hello, World!")
    funcWithCallback(lambda timestamp: print("Current timestamp: {}".format(timestamp)))

    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # converted = list(map(FahrenheitToCelsius, ftemps))
    # We can use lambdas in place of function definitions
    converted = list(map(lambda f: (f - 32) * 5 / 9, ftemps))
    print(ftemps)
    print(converted)

    celsiusToFahrenheit = lambda c: (c * 9 / 5) + 32
    converted = list(map(celsiusToFahrenheit, ctemps))
    print(ctemps)
    print(converted)


if __name__ == "__main__":
    main()
