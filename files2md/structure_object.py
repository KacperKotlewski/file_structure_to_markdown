class StructureObject:
    def __init__(self, name="", dir=""):
        self.name = name
        self.dir = dir
        self.type = type(self)

    def getName(self): return self.name
    def getDir(self): return self.dir
    def getType(self): return self.type