def parseFile(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return [name.replace('"', "").strip() for name in text.split(",")]


names = sorted(parseFile(r"./project_22_names.txt"))


def getNameScore(name):
    return sum([ord(letter) - 64 for letter in list(name)])


def getFileScore(names):
    scores = 0
    for i, name in enumerate(names):
        scores += (i + 1) * getNameScore(name)
    return scores


print(getFileScore(names))
