from .user_input import UserInput

import colorama
from colorama import Fore, Back, Style

class ToMarkdownFile:
    def __init__(self, str_to_save:str, path:str=".", filename:str="README2.md", mode:str="x", questions:bool=True):
        self.content = str_to_save
        self.conf = {
            "fileStart":"<!-- files2md start -->",
            "fileEnd":"<!-- files2md end -->",
            "path" : path,
            "filename" : filename,
            "mode" : mode,
            "questions" : questions,
        }
        self.userInp = UserInput(tryAgain=UserInput.tryAgain["try"])
        self.col = colorama.init()

    def save(self):
        self.conf["filename"] = self._checkFilename(self.conf["filename"])
        if(self.conf["mode"] != None):
            file = open(self.conf["filename"], self.conf["mode"])
            file.write(self.content)
            file.close()

    def _checkFilename(self, name:str):
        if self._isDetecting(name) and self.conf["questions"]:
            name = self._getModeFromUser(name)
        else:
            return name


    def _getModeFromUser(self, name:str):

        print(Fore.RED + f"{name} detected!" + Style.RESET_ALL)
        if self.userInp.restricted(restricted_inputs=["y","n"], to_print="You want to set new filename?", anyCase=True) == "n":
            if self.userInp.restricted(restricted_inputs=["y","n"], to_print="You want to overwrite it?", anyCase=True) == "n":
                if self.userInp.restricted(restricted_inputs=["y","n"], to_print="You want to insert this file structure into existing file?", anyCase=True) == "y":
                    self.conf["mode"] = "a"
                else:
                    self.conf["mode"] = None
            else:
                self.conf["mode"] = "w"
        else:
            name = self.userInp.normal(to_print="Set new file name", statment=self._isDetecting, invertedStatment=True)
        return name

    def _isDetecting(self, name): import os; return ( len( [file for file in os.listdir(self.conf["path"]) if file == name ] ) != 0 )