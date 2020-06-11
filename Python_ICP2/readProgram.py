inputFile = open("input.txt", "r")

data = inputFile.read()

data = data.split()

print(data)

wordList = {}

for word in data:

    word = word.casefold()

    if word not in wordList:

        wordList[word] = 0

    wordList[word] += 1

print(wordList)



with open('input.txt', 'a') as file:

    for key in wordList:

        file.write(str(key) + " : " + str(wordList[key]) + "\r\n")