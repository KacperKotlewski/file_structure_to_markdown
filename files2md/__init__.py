import files2md.config
import files2md.structure_objects

def list():
    from files2md.structure_objects import DirectoryObj
    dir = DirectoryObj(name="projekt", dir=".")
    dir.autoAddFile(autoAddSubdirs=True)
    print(dir.getTree())


if __name__ == "__main__":
    list()