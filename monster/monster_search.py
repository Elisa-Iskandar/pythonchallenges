f = open("monster_simple.txt", "r")
monsterDict = {}
next(f)
for lines in f:
    thisLine = lines.split(",")
    monsterDict[thisLine[0]] = thisLine[1]

def search(monsterName):
    return monsterDict.get(monsterName, "Monster not in list")

print(search("Aatxe"))
print(search("Not a monster"))
f.close()
