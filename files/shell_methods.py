import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")

        # Make a backup copy
        dst = src + ".bak"

        # copy ofer the permissions, modification times, and other info
        shutil.copy(src, dst)
        shutil.copystat(src, dst)  # metadata

        # rename the original file
        os.rename("textfile.txt", "newfile.txt")

        # put contents into an archive
        root_dir, tail = path.split(src)
        # make_archive("archive", format="zip", root_dir=root_dir)

        # MOre fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == "__main__":
    main()
