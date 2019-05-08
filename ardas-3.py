import os
import tarfile
import re

folder = []
#list for objects which will be deleted
temp = []

os.chdir(r'./tempdir')
print(os.getcwd())
tar = tarfile.open("archive.tar.gz", "w:gz")

for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        folder.append(subdirname)

for item in folder:
    if (re.match(r'2016', item)) or (re.match(r'\d{4}', item)) is not None:
        temp.append(item)
        item = item+"/"
        print(item)
        tar.add(item, recursive=True)
tar.close()

for item in temp:
    os.rmdir(item)
