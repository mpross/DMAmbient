import os
import string

tavernCount=0
dungeonCount=0
townCount=0
noneCount=0

fileIndex=0

directory = 'corpus/FINAL TEXT FILES/'

for filename in os.listdir(directory):

    rawData = open(directory + filename).read()
    rawData = rawData.lower()
    rawData = rawData.translate(str.maketrans('', '', string.punctuation))
    rawData = rawData.replace('\n', ' ')
    rawData = rawData.split(' ')

    data=[]
    outdata=[]

    dungeonWords = ['dungeon', 'cave', 'mine', 'dark', 'damp']
    townWords = ['town', 'crowds', 'road', 'street', 'crowd', 'buildings', 'tent']
    tavernWords = ['tavern', 'drunk', 'tankard', 'bar', 'barkeep', 'inn', 'beds']

    chunkSize = 100

    for chunkIndex in range(round(len(rawData)/chunkSize)):

        foundBool = False

        chunk = rawData[chunkIndex*chunkSize:(chunkIndex+1)*chunkSize]

        for wordIndex in range(len(chunk)):
            for word in tavernWords:

                if (chunk[wordIndex] == word) & (foundBool == False):
                    tavernCount += 1
                    data.append('\ntavern\t')
                    for i in range(len(chunk)):
                        data.append(chunk[i])
                    foundBool = True
                    break

            for word in dungeonWords:
                if (chunk[wordIndex] == word) & (foundBool == False):
                    dungeonCount += 1
                    data.append('\ndung\t')
                    for i in range(len(chunk)):
                        data.append(chunk[i])
                    foundBool = True
                    break

            for word in townWords:
                if (chunk[wordIndex] == word) & (foundBool == False):
                    townCount += 1
                    data.append('\ntown\t')
                    for i in range(len(chunk)):
                        data.append(chunk[i])
                    foundBool = True
                    break

        if foundBool == False:

            data.append('\nnone\t')
            for i in range(len(chunk)):
                data.append(chunk[i])
            noneCount+=1

    fileIndex += 1

    # if fileIndex >=2:
    #     break


    for i in range(len(data)):
        outdata.append(data[i])
        outdata.append(' ')

    print(''.join(outdata))

    file=open('corpus/tagged/'+str(fileIndex)+'.txt', 'w+').write(''.join(outdata))

print(tavernCount)
print(dungeonCount)
print(townCount)
print(noneCount)
