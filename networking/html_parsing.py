import urllib.request
from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print("Encountered comment: {}".format(data))
        pos = self.getpos()
        print("\tAt line {} position {}".format(pos[0], pos[1]))

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            global metacount
            metacount += 1
        print("Encountered start of tag: {}".format(tag))
        pos = self.getpos()
        print("\tAt line {} position {}".format(pos[0], pos[1]))

        if attrs.__len__() > 0:
            print("\tAttributes: ")
            for a in attrs:
                print("\t - {} = {}".format(a[0], a[1]))

    def handle_endtag(self, tag):
        print("Encountered end of tag: {}".format(tag))
        pos = self.getpos()
        print("\tAt line {} position {}".format(pos[0], pos[1]))

    def handle_data(self, data):
        if (data.isspace()):
            return
        print("Encountered data: {}".format(data))
        pos = self.getpos()
        print("\tAt line {} position {}".format(pos[0], pos[1]))

    def error(self, message):
        pass


def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)
    print("Meta tags found: {}".format(metacount))


if __name__ == "__main__":
    main()
