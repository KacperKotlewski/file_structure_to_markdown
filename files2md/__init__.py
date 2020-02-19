import os
from files2md.directory import DirectoryObj

def list():
    dir = DirectoryObj(name=".", dir=".")
    print(dir.getName())
    dir.autoAddFile(autoAddSubdirs=True)
    dir.getSubdirsAndFiles()
    for d in dir.files:
        print(d.getName())

if __name__ == "__main__":
    list()