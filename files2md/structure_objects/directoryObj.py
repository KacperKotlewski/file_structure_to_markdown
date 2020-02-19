from files2md.structure_objects.appendSubdirs import AppendSubdirs
from files2md.structure_objects.buildFilesTree import  BuildFilesTree
from files2md.structure_objects.structureObject import StructureObject
from files2md import config

class DirectoryObj(StructureObject):
    def __init__(self, dir, name):
        super().__init__(name=name, dir=dir)
        self.files = []

    def addFile(self, file:StructureObject):
        if not config.isIgnored(file):
            self.files.append(file)

    def getFiles(self):
        return self.files

    def getByDir(self, dir):
        return [f for f in self.files if f.dir == dir][0]

    def autoAddFile(self, autoAddSubdirs=False):
        AppendSubdirs(self)
        if(autoAddSubdirs):
            for d in self.files:
                if d.getType() == DirectoryObj:
                    d.autoAddFile(autoAddSubdirs=True)

    def getTree(self):
        return BuildFilesTree(self)