uniqueWords = set()
file = open("input.txt", 'r')
allWords = file.read().split()
for i in allWords:
  uniqueWords.add(i)
print(len(uniqueWords))
