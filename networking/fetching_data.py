import urllib.request


def main():
    web_url = urllib.request.urlopen("https://www.google.com/")
    print("Result code: {}".format(web_url.getcode()))

    if web_url.getcode() == 200:
        data = web_url.read()
        print(data)


if __name__ == "__main__":
    main()
