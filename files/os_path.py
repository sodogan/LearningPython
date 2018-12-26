import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("Item exists: {}".format(str(path.exists("textfile.txt"))))
    print("Item is a file: {}".format(path.isfile("textfile.txt")))
    print("Item is a directory: {}".format(path.isdir("textfile.txt")))

    # Work with file paths
    print("Item path: {}".format(path.realpath("textfile.txt")))
    print("Item path and name: {}".format(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print("Item modification time: {}".format(t))
    t2 = datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("Item modification time: {}".format(t2))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - t2
    print("Item has been {} since the file was modified".format(td))
    print("Item has been {} seconds since the file was modified".format(td.total_seconds()))


if __name__ == "__main__":
    main()
