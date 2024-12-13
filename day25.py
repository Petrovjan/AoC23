import copy
data = open("day25.txt").read().split("\n")
for i in range(len(data)):
    data[i] = data[i].split()
print(data)
sone = "gql"
stwo = "kht"

nodeDict = dict()
for j in range(len(data)):
    if data[j][0] in nodeDict.keys():
        curval = copy.deepcopy(nodeDict.get(data[j][0]))
        curval+= data[j][1:]
        nodeDict[data[j][0]] = curval
    else:
        nodeDict[data[j][0]] = data[j][1:]
    for nd in range(1,len(data[j])):
        if data[j][nd] in nodeDict.keys():
            cv = copy.deepcopy(nodeDict.get(data[j][nd]))
            cv.append(data[j][0])
            nodeDict[data[j][nd]] = cv
        else:
            nodeDict[data[j][nd]] = [data[j][0]]

print(nodeDict)
def countNodes(nodeDict, start):
    next = [start]
    visited = set()
    while len(next) > 0:
        newnext = []
        for node in next:
            if node in nodeDict.keys():
                possnodes = nodeDict.get(node)
                for pn in possnodes:
                    if pn not in visited:
                        newnext.append(pn)
            visited.add(node)
        next = copy.deepcopy(newnext)
    return len(visited)



a = countNodes(nodeDict, sone)
b = countNodes(nodeDict, stwo)
print(a)
print(b)
print(a*b)

# rmt -> nqh
# ltn -> trh
# psj -> fdb
#
# sone = "gql"
# stwo = "kht"