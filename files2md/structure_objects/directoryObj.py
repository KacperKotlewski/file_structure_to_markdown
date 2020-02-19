from .structureObject import StructureObject
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

    def getTree(self, dirprefix=""):
        return BuildFilesTree(self, dirprefix)
        pass


def AppendSubdirs(dir_obj:DirectoryObj):
    import os
    for dirname, dirnames, filenames in os.walk(dir_obj.getDir()):
        obj = None
        from files2md.structure_objects.file import FileObj
        for filename in filenames:
            obj = FileObj(name=filename, dir=dirname)
            dir_obj.addFile(obj)

        for subdirname in dirnames:
            obj = DirectoryObj(name=subdirname, dir=str(os.path.join(dirname, subdirname)))
            dir_obj.addFile(obj)

        break


def BuildFilesTree(dir_obj:DirectoryObj, dirprefix):
    result=""
    pref = ((dirprefix[:-1] + "-") if (dirprefix != "") else "")
    result += (pref + dir_obj.getName() +"\n")
    dirprefix += "| "
    for d in dir_obj.files:
        if d.getType() == DirectoryObj:
            result += d.getTree(dirprefix)
        else:
            result += (dirprefix + d.getName() +"\n")
    return result