import copy

data = open("day21.txt").read().split("\n")
for d in range(len(data)):
    data[d] = [x for x in data[d]]
print(data)

srow = 0
scol = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            srow = i
            scol = j

data[srow][scol] = "."
# srow = len(data)-1
# scol = len(data)-1
data[srow][scol] = "E"

switchScreen = (len(data)+1)/2

odd = dict()
even = dict()
even[(srow,scol)] = 0
possdir = [(-1,0),(0,1),(1,0),(0,-1)]
nextDict = dict()
last = [(srow,scol)]

fillDict = dict()

r = 0
while len(last) > 0:
    r += 1
    next = copy.deepcopy(last)
    nextDict.clear()
    for pos in last:
        next.remove(pos)
        for dir in possdir:
            nfrow = pos[0] + dir[0]
            nfcol = pos[1] + dir[1]
            if nfrow < 0 or nfcol < 0 or nfrow >= len(data) or nfcol >= len(data[0]):
                continue
            if (nfrow, nfcol) not in odd.keys() and (nfrow, nfcol) not in even.keys() and (nfrow, nfcol) not in nextDict.keys():
                if data[nfrow][nfcol] == ".":
                    next.append((nfrow, nfcol))
                    nextDict[(nfrow, nfcol)] = r
                    if r%2 == 0:
                        even[(nfrow, nfcol)] = r
                        data[nfrow][nfcol] = "E"
                    else:
                        odd[(nfrow, nfcol)] = r
                        data[nfrow][nfcol] = "O"
    last = next

    countE = 0
    countO = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "E":
                countE += 1
            elif data[i][j] == "O":
                countO += 1

    fillDict[r] = (countE, countO)
print(r)

countE = 0
countO = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "E":
            countE += 1
        elif data[i][j] == "O":
            countO += 1
print(countE, countO, countO + countE)
print(fillDict)

steps = 26501365 - 65
reps = int(steps/131)
halfrep = int(reps/2)
print(reps)

count = 7423
n = 0
small = 4
large = 0
for r in range(2,reps):
    n += 4
    if r%2 != 0:
        count += n*7423
    else: count += n*7490
    small += 4
    large += 4
print(n, count)


result = 7423 + (halfrep*4 + 0.5 * halfrep * 8 * (halfrep - 1))*7490 + (halfrep*8 + 0.5 * halfrep * 8 * (halfrep - 1))*7423
result = count + (5744+5708+5693+5729) + small * (900) + large * (6520)
print(int(result))

print(result - 610321885082978)