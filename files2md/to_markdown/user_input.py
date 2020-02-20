import colorama
from colorama import Fore, Back, Style
class UserInput():
    def __init__(self, after=None, tryAgain=None):
        self.col = colorama.init()
        self.after = after
        self.tryAgain = tryAgain

    def restricted(self, restricted_inputs:list, anyCase=False, to_print:str="", after=None, tryagain=None):
        out = None
        while True:
            inpInStr = str('/'.join(map(str, restricted_inputs)))
            print(Fore.YELLOW + f"{to_print} ({inpInStr}): ", end = '')
            i = input()
            print(Style.RESET_ALL, end = '')

            inp = i
            if anyCase:
                inp = inp.lower()
                restricted_inputs = [inp.lower() for inp in restricted_inputs]

            if inp in restricted_inputs:
                out = i
                break
            else:
                self._printTry(tryagain)
        self._runAfter(after)
        return out

    def normal(self, lowerCase=False, to_print:str="", after=None, tryagain=None, statment=None, addirionalStatmentArgs=None, invertedStatment:bool=False):
        out = None
        while True:
            print(Fore.YELLOW + f"{to_print}: ", end = '')
            i = input()
            print(Style.RESET_ALL, end = '')

            i = i[-3:]+".md" if i[-3:].lower() == ".md" else i+".md"
            inp = i
            if lowerCase:
                inp = inp.lower()
            if statment == None:
                out=inp
                break
            elif invertedStatment:
                if not statment(inp, **addirionalStatmentArgs):
                    out=inp
                    break
                else:
                    self._printTry(tryagain)
            else:
                if statment(inp, **addirionalStatmentArgs):
                    out=inp
                    break
                else:
                    self._printTry(tryagain)
        self._runAfter(after)
        return out

    def _runAfter(self, after):
        if after == None:
            after = self.after
        if type(after) == str:
            print(after)

    def _printTry(self, try_again):
        if try_again == None:
            try_again = self.tryAgain
        if type(try_again) == str:
            print(try_again)

    after = {"ok" : (Fore.LIGHTGREEN_EX + "OK" + Style.RESET_ALL) }
    tryAgain = {"try" : (Fore.RED + "Try again!" + Style.RESET_ALL)}