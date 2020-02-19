import files2md.config
import files2md.structure_objects
from files2md.config import config, isIgnored
from files2md.structure_objects.directoryObj import DirectoryObj
from files2md.structure_objects.file import FileObj
from files2md.structure_objects.structureObject import StructureObject
from files2md.structure_objects.buildFilesTree import BuildFilesTree
from files2md.structure_objects.appendSubdirs import AppendSubdirs

def list():
    dir = DirectoryObj(name="projekt", dir=".")
    dir.autoAddFile(autoAddSubdirs=True)
    dir.getTree()


if __name__ == "__main__":
    list()