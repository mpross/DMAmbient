rawData = open("corpus/C1E002_FINAL.txt").read()
rawData = rawData.replace('\n',' ')
rawData = rawData.split(' ')

tavernIndex=[]
dungeonIndex=[]
townIndex=[]

dungeonWords=['dungeon','cave','mine']
townWords=['town']
tavernWords=['tavern','drunk']

buffer=10

for i in range(len(rawData)):
    for word in tavernWords:
        if (rawData[i]==word):
            tavernIndex.append(i)
            rawData.insert(i-buffer,'/tavern')

    for word in dungeonWords:
        if (rawData[i]==word):
            dungeonIndex.append(i)
            rawData.insert(i - buffer, '/dung')

    for word in townWords:
        if (rawData[i] == word):
            townIndex.append(i)
            rawData.insert(i - buffer, '/town')

print(''.join(rawData).split('/'))
