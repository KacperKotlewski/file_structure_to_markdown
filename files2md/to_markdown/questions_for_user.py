import colorama
from colorama import Fore, Back, Style

def getModeAndFilenameFromUser(name: str, path:str, mode: str):
    colorama.init()
    print(Fore.RED + f"{name} detected!" + Style.RESET_ALL)
    from .user_input import UserInput
    userInp = UserInput()
    if userInp.restricted(restricted_inputs=["y", "n"], to_print="You want to set new filename?",
                               anyCase=True).lower() == "n":
        if userInp.restricted(restricted_inputs=["y", "n"], to_print="You want to overwrite it?",
                                   anyCase=True).lower() == "n":
            if userInp.restricted(restricted_inputs=["y", "n"],
                                       to_print="You want to insert this file structure into existing file?",
                                       anyCase=True).lower() == "y":
                    mode = "a"
                # if self.userInp.restricted(restricted_inputs=["y", "n"], to_print="Replace old structure tree if exist?", anyCase=True).lower() == "y": self.conf["replace"] = True
            else:
                mode = None
        else:
            mode = "w"
    else:
        name = userInp.normal(to_print="Set new file name", statment=isDetecting, addirionalStatmentArgs={"path":path}, invertedStatment=True)
        print(name)
    return {"filename":name, "mode":mode}


def isDetecting(name:str, path:str): import os; return ( len( [file for file in os.listdir(path) if file == name ] ) != 0 )