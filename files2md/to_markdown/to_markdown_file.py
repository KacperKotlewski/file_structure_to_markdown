from .user_input import UserInput

class ToMarkdownFile:
    def __init__(self, str_to_save:str, path:str=".", filename:str="README.md", mode:str="w", questions:bool=True):
        self.conf = {
            "fileStart":"<!-- files2md start -->",
            "fileEnd":"<!-- files2md end -->",
            "content" : str_to_save,
            "path" : path,
            "filename" : filename,
            "saveMode" : mode,
            "questions" : questions,
        }
        self.userInp = UserInput(after=UserInput.after["ok"], tryAgain=UserInput.tryAgain["try"])

    def __call__(self):
        self.save()

    def save(self):
        if self._isDetecting() and self.conf["questions"]:
            self._getModeFromUser()


    def _getModeFromUser(self):
        import colorama
        from colorama import Fore, Back, Style
        colorama.init()

        print(Fore.RED + f"{self.conf['filename']} detected!" + Style.RESET_ALL)
        if self.userInp.restricted(restricted_inputs=["y","n"], to_print="You want to set new filename?", anyCase=True) != "y":
            if self.userInp.restricted(restricted_inputs=["y","n"], to_print="You want to overwrite it?", anyCase=True) != "y":
                self.conf["mode"] = "a"
        else:
            input(Fore.YELLOW + "Set new file name: ")
            print(Style.RESET_ALL)

    def _isDetecting(self): import os; return ( len( [file for file in os.listdir(self.conf["path"]) if file == self.conf["filename"] ] ) != 0 )