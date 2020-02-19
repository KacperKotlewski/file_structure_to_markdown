from files2md.directory import DirectoryObj

def list():
    dir = DirectoryObj(name="projekt", dir=".")
    dir.autoAddFile(autoAddSubdirs=True)
    dir.getSubdirsAndFiles()