def parseFile(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return [name.replace('"', "").strip() for name in text.split(",")]

data = parseFile(r"./problem_42_words.txt")

def getWordValue(word):
  i = 0
  for c in word:
    i += ord(c) - 64
  return i

def countTriangleWords(words):
  wordValues = [getWordValue(word) for word in words]
  maxValue = max(wordValues)
  memory = set()

  start = (1,1)
  while start[1] <= maxValue:
    memory.add(start[1])
    start = (start[0] + 1, (start[0] + 1)**2 - start[1])

  triangleWords = [wordValue for wordValue in wordValues if wordValue in memory]
  return len(triangleWords)

print(countTriangleWords(data))
