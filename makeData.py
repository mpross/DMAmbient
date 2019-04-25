import nltk
import os
import string

tavernIndex = []
dungeonIndex = []
townIndex = []

fileIndex=0

directory = 'corpus/FINAL TEXT FILES/'

for filename in os.listdir(directory):

    rawData = open(directory + filename).read()
    rawData = rawData.lower()
    rawData = rawData.translate(str.maketrans('', '', string.punctuation))
    rawData = rawData.replace('\n', ' ')
    rawData = rawData.split(' ')

    dungeonWords = ['dungeon', 'cave', 'mine', 'dark', 'damp']
    townWords = ['town', 'crowds', 'road', 'street', 'crowd', 'buildings', 'tent']
    tavernWords = ['tavern', 'drunk', 'tankard', 'bar', 'barkeep', 'inn', 'beds']

    buffer = 10

    for chunkIndex in range(round(len(rawData)/buffer)):

        foundBool = False

        chunk = rawData[chunkIndex*buffer:(chunkIndex+1)*buffer]

        for wordIndex in range(len(chunk)):
            for word in tavernWords:

                if (chunk[wordIndex] == word) & (foundBool == False):
                    tavernIndex.append(wordIndex)
                    rawData.insert(chunkIndex*buffer, '/tavern/')
                    foundBool = True
                    break

            for word in dungeonWords:
                if (chunk[wordIndex] == word) & (foundBool == False):
                    dungeonIndex.append(wordIndex)
                    rawData.insert(chunkIndex*buffer, '/dung/')
                    foundBool = True
                    break

            for word in townWords:
                if (chunk[wordIndex] == word) & (foundBool == False):
                    townIndex.append(wordIndex)
                    rawData.insert(chunkIndex*buffer, '/town/')
                    foundBool = True
                    break

        if foundBool == False:
            rawData.insert(chunkIndex*buffer, '/none/')

    fileIndex += 1

    if fileIndex >=2:
        break


    print(''.join(rawData))

print(len(tavernIndex))
print(len(dungeonIndex))
print(len(townIndex))
