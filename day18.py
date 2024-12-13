import copy

raw = open("day18.txt").read().split("\n")

sumup = 0
sumdown = 0
sumleft = 0
sumright = 0
data = []
for r in range(len(raw)):
    data.append(raw[r].split())
    if data[-1][0] == "U":
        sumup += int(data[-1][1])
    elif data[-1][0] == "D":
        sumdown += int(data[-1][1])
    elif data[-1][0] == "R":
        sumright += int(data[-1][1])
    elif data[-1][0] == "L":
        sumleft += int(data[-1][1])

print(data)
print(sumup, sumdown, sumright, sumleft)

f = ["." for x in range(2000)]
field = [f[:] for y in range(2000)]
field[1000][1000] = "#"

cfield = copy.deepcopy(field)

dirDict = dict()
dirDict["R"] = (0,1)
dirDict["L"] = (0,-1)
dirDict["U"] = (-1,0)
dirDict["D"] = (1,0)

old = field[0][903]

dig = [1000, 1000]
for i in range(len(data)):
    for c in range(int(data[i][1])):
        direction = dirDict.get(data[i][0])
        dig[0] += direction[0]
        dig[1] += direction[1]
        if cfield[0][903] != old:
            pass
        cfield[dig[0]][dig[1]] = "#"


for k in range(len(cfield)):
    for l in range(len(cfield[k])):
        if k == 0 or k == len(cfield) - 1:
            cfield[k][l] = "X"
        elif l == 0 or l == len(cfield[k]) - 1:
            cfield[k][l] = "X"

void = [[1,1]]

while len(void) > 0:
    v = void.pop()
    for d in dirDict.values():
        if cfield[v[0]+d[0]][v[1]+d[1]] == ".":
            cfield[v[0] + d[0]][v[1] + d[1]] = "X"
            void.append([v[0]+d[0],v[1]+d[1]])

result = 0
for m in range(len(cfield)):
    for n in range(len(cfield[m])):
        if cfield[m][n] in "#.":
            result += 1

print(result)
