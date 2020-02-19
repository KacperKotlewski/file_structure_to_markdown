from files2md.structure_object import StructureObject
class DirectoryObj(StructureObject):
    def __init__(self, dir, name):
        super().__init__(name=name, dir=dir)
        self.type = type(self)
        self.files = []

    def addFile(self, file):
        if(type(file) == StructureObject):
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
                    d.autoAddFile(True)

    def getSubdirsAndFiles(self):
        for d in self.files:
            print(d.getName())
            if d.type == DirectoryObj:
                d.getSubdirsAndFiles()

    def _autoListDirsInside(self):
        import os
        for dirname, dirnames, filenames in os.walk(self.getDir()):
            obj = None
            for subdirname in dirnames:
                obj = DirectoryObj(name=subdirname, dir=dirname)

            from files2md.file import FileObj
            for filename in filenames:
                obj = FileObj(name=filename, dir=dirname)

            if(obj != None):
                print(obj.getName())
                self.addFile(obj)

            if '.git' in dirnames:
                dirnames.remove('.git')
                dirnames.remove('.idea')
            break