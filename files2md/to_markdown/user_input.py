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
            i = input(f"{to_print} ({inpInStr}): ")
            if anyCase:
                i = i.lower()
                restricted_inputs = [inp.lower() for inp in restricted_inputs]

            if i in restricted_inputs:
                out = i
                break
            else:
                self._printTry(tryagain)
        self._runAfter(after)
        return out

    def _runAfter(self, after):
        if after == None:
            after = self.after

        if type(after) == type(self._after_OK):
            after()
        elif type(after) == str:
            print(after)

    def _printTry(self, try_again):
        if try_again == None:
            try_again = self.tryAgain

        if type(try_again) == type(self._after_OK):
            try_again()
        elif type(try_again) == str:
            print(try_again)

    def _after_OK(self): print(Fore.GREEN + "OK")
    after_OK = _after_OK