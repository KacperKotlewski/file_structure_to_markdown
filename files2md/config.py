config = {
    "ignore": [".git", ".idea", "build", "dist", "*.egg-info", "__pycache__"],
    }

def isIgnored(filename:str):
    for ignored in config["ignore"]:
        if ignored == filename:
            return True
        elif len([char for char in ignored if char == "*"]) != 0:
            ignoreValues = [""]
            for index, char in enumerate(ignored):
                if char == "*" and index != 0: ignoreValues[len(ignoreValues)] = ""
                elif char != "*": ignoreValues[len(ignoreValues)-1] += char

            contain = True
            for val in ignoreValues:
                if not filename.__contains__(val): contain = False
            if contain: return True
    return False