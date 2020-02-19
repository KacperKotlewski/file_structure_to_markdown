import files2md
import files2md.config
import files2md.structure_objects
import files2md.to_markdown

def tree2md():
    from files2md.structure_objects import DirectoryObj
    from files2md.to_markdown import ToMarkdownFile
    import os
    currentDir = os.getcwd()
    currentDirName = str(os.path.basename(currentDir))

    dir = DirectoryObj(name=currentDirName, dir=currentDir)
    dir.autoAddFile(autoAddSubdirs=True)
    ToMarkdownFile(dir.getTree()).save()


if __name__ == "__main__":
    tree2md()