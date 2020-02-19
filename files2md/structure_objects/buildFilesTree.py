import files2md.structure_objects as directory

def BuildFilesTree(dir_obj, dirprefix=""):
    result=""
    pref = ((dirprefix[:-1] + "-") if (dirprefix != "") else "")
    result += (pref + dir_obj.getName() +"\n")
    dirprefix += "| "
    for d in dir_obj.files:
        if d.getType() == directory.DirectoryObj:
            d.getSubdirsAndFiles(dirprefix)
        else:
            result += (dirprefix + d.getName() +"\n")
    return result