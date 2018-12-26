def main():
    # Open file in write mode (w+)
    f = open("textfile.txt", "w+")
    f.write("Hello, World!")
    f.close()

    # Open the file for appending text to the end instead of overwriting
    f = open("textfile.txt", "a")

    for i in range(10):
        f.write("This is line {line_number} \r\n".format(line_number=i))
    f.close()

    # Open the file for read access
    f = open("textfile.txt", "r")
    if f.mode == 'r':
        # Successfully opened file for read
        # contents = f.read()
        # print(contents)

        # Read line-by-line
        fl = f.readlines()
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()
