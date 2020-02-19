import files2md.config
import files2md.structure_objects
import files2md.to_markdown

def tree2md():
    from files2md.structure_objects import DirectoryObj
    from files2md.to_markdown import ToMarkdownFile
    import os
    currentDir = os.getcwd()
    currentDirName = str(os.path.basename(currentDir))

    md = ToMarkdownFile("xd")
    md()

    dir = DirectoryObj(name=currentDirName, dir=currentDir)
    dir.autoAddFile(autoAddSubdirs=True)
    print(dir.getTree())


if __name__ == "__main__":
    tree2md()