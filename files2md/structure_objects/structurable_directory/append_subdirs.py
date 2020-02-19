from .directoryObj import DirectoryObj

def appendSubdirs(dir_obj:DirectoryObj):
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