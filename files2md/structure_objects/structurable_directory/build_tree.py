from .directoryObj import DirectoryObj

def buildFilesTree(dir_obj:DirectoryObj, dirprefix):
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