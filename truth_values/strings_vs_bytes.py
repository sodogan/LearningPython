# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # print(s + b) TypeError: can only concatenate str (not "bytes") to str
    # Need first to decode bytes as string
    s2 = b.decode('utf-8')
    print(s + s2)

    b2 = s.encode('utf-8')
    print(b2)
    print(b + b2)

    print(s.encode('utf-32'))


if __name__ == "__main__":
    main()
