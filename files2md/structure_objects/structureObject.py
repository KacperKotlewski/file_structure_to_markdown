class StructureObject:
    def __init__(self, name="", dir=""):
        self.name = name
        self.dir = dir

    def getName(self): return self.name
    def getDir(self): return self.dir
    def getType(self): return type(self)