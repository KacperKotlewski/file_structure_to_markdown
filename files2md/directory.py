from files2md.structure_object import StructureObject
from files2md import config
class DirectoryObj(StructureObject):
    def __init__(self, dir, name):
        super().__init__(name=name, dir=dir)
        self.type = type(self)
        self.files = []

    def addFile(self, file:StructureObject):
        if not config.isIgnored(file.getName()):
            self.files.append(file)

    def getFiles(self):
        return self.files

    def getByDir(self, dir):
        return [f for f in self.files if f.dir == dir][0]

    def autoAddFile(self, autoAddSubdirs=False):
        self._autoListDirsInside()
        if(autoAddSubdirs):
            for d in self.files:
                if d.type == DirectoryObj and autoAddSubdirs:
                    d.autoAddFile(autoAddSubdirs=True)

    def getSubdirsAndFiles(self, dirprefix=""):
        pref  = ((dirprefix[:-1]+"-") if (dirprefix != "") else "")
        print(pref+self.getName())
        dirprefix += "| "
        for d in self.files:
            if d.type == DirectoryObj:
                d.getSubdirsAndFiles(dirprefix)
            else:
                print(dirprefix+d.getName())

    def _autoListDirsInside(self):
        import os
        for dirname, dirnames, filenames in os.walk(self.getDir()):
            obj = None
            for subdirname in dirnames:
                obj = DirectoryObj(name=subdirname, dir=str(os.path.join(dirname, subdirname)))
                self.addFile(obj)

            from files2md.file import FileObj
            for filename in filenames:
                obj = FileObj(name=filename, dir=dirname)
                self.addFile(obj)
            break