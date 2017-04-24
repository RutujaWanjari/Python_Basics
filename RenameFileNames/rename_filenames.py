# This program demonstrates how to access files from relative path.
# Also it changes alphanumeric file names to totally alphabetic names.
# To successfully run this program create a directory "AllFiles" and add multiple files with alphanumeric names.

from pathlib import Path
import os

# Path is a class from "pathlib" package. Below we are calling init() function of Path class which initializes it and
# makes some memory for our work.
p = Path('../RenameFileNames/AllFiles/')


def rename():
    for x in p.iterdir():
        if x.is_file():
            print(x.name)
            file = x.name
            result = ''.join([i for i in file if not i.isdigit()])

            # rename is a function from "os" package
            rename(os.path.join(p, x.name), os.path.join(p, result))


def print_output():
    for x in p.iterdir():
        print(x.name)

rename()
print_output()
