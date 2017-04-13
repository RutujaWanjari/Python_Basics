# This program demonstrates how to access files from relative path.
# Also it changes alphanumeric file names to totally alphabetic names

from pathlib import Path
import os

p = Path('../RenameFileNames/AllFiles/')

for x in p.iterdir():
    if x.is_file():
        print(x.name)
        file = x.name
        result = ''.join([i for i in file if not i.isdigit()])
        os.rename(os.path.join(p, x.name), os.path.join(p, result))

for x in p.iterdir():
    print(x.name)
