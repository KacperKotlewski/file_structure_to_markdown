import files2md.config
import files2md.structure_objects
import files2md.structurable_directory

def list():
    dir = files2md.structurable_directory.DirectoryObj(name="projekt", dir=".")
    dir.autoAddFile(autoAddSubdirs=True)
    print(dir.getTree())


if __name__ == "__main__":
    list()