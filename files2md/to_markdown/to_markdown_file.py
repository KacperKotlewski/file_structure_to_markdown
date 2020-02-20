from .user_input import UserInput

class ToMarkdownFile:
    def __init__(self, str_to_save:str, path:str=".", filename:str="file_structure.md", mode:str="x", questions:bool=True, replace:bool=False):
        self.conf = {
            "title":"## File Structure",
            "fileStart":"<!-- files2md start -->",
            "fileEnd":"<!-- files2md end -->",
            "path" : path,
            "filename" : filename,
            "mode" : mode,
            "questions" : questions,
            "replace" : replace,
        }
        self.content = self.conf["fileStart"] + "\n" + self.conf["title"] + "\n```\n" + str_to_save + "```\n" + self.conf["fileEnd"]
        self.userInp = UserInput(tryAgain=UserInput.tryAgain["try"])

    def save(self):
        rename = self._checkFilename(self.conf["filename"], self.conf["mode"])
        self.conf["filename"] = rename["filename"]
        self.conf["mode"] = rename["mode"]
        if(self.conf["mode"] != None):
            file = open(self.conf["filename"], self.conf["mode"])
            file.write(self.content)
            file.close()

    def _checkFilename(self, name:str, mode:str):
        from .questions_for_user import getModeAndFilenameFromUser, isDetecting
        if isDetecting(name=name, path=self.conf["path"]) and self.conf["questions"]:
            return getModeAndFilenameFromUser(name=name, path=self.conf["path"], mode=mode)
        else:
            return {"filename":name, "mode":mode}