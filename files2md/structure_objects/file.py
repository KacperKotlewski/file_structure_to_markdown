from files2md.structure_objects import StructureObject

class FileObj(StructureObject):
    def __init__(self, dir, name):
        super().__init__(name=name, dir=dir)