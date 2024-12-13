import copy
from functools import cache

data = open("day14.txt").read().split("\n")
cdata = copy.deepcopy(data)

fdata = []
for i in range(len(cdata)):
    for j in range(len(cdata[i])-1,-1,-1):
        if len(fdata) <= i:
            fdata.append(cdata[i][j])
        elif len(fdata) < len(cdata[i]):
            fdata.append(cdata[i][j])
        else:
            fdata[len(cdata) - j - 1] = fdata[len(cdata) - j - 1][:] + cdata[i][j]

@cache
def rotateCW(data):
    data = list(data)
    fdata = []
    for m in range(len(data)):
        fdata.append("")
    for i in range(len(data)-1,-1,-1):
        for j in range(len(data[i])-1,-1,-1):
                fdata[j] = fdata[j][:] + data[i][j]
    return tuple(fdata)

@cache
def shiftBalls(oneline):
    availspots = []
    for s in range(len(oneline)):
        if oneline[s] == ".":
            availspots.append(s)
        elif oneline[s] == "#":
            availspots.clear()
        elif oneline[s] == "O":
            if len(availspots) > 0:
                ball = availspots.pop(0)
                oneline = oneline[:ball] + "O" + oneline[ball+1:]
                oneline = oneline[:s] + "." + oneline[s+1:]
                availspots.append(s)
    return oneline

@cache
def fall(olddata):
    newdata = []
    for i in range(len(olddata)):
        newdata.append(shiftBalls(olddata[i]))
    return newdata


ndata = tuple(fall(tuple(fdata)))
dedupl = []
rng = 1000000000
skip = True
n = 1
while n <= rng:
    if n != 1:
        ndata = tuple(fall(rotateCW(edata)))
    wdata = tuple(fall(rotateCW(ndata)))
    sdata = tuple(fall(rotateCW(wdata)))
    edata = tuple(fall(rotateCW(sdata)))

    if n%1000 == 0:
        dedupl = edata
    if edata == dedupl and n>1000 and skip:
        skip = False
        dedper = n - 1000
        reduceby = int((rng - 1000)/dedper)*dedper
        n += int((rng - 1000)/dedper)*dedper
    n += 1

result = 0
for y in range(len(edata)):
    for k in range(len(edata[y])):
        if edata[y][k] == "O":
            result += y+1
print("part2: ",result)