from files2md.structure_objects.directory import DirectoryObj

def list():
    dir = DirectoryObj(name="projekt", dir=".")
    dir.autoAddFile(autoAddSubdirs=True)
    dir.getSubdirsAndFiles()


if __name__ == "__main__":
    list()