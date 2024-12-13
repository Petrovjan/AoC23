raw = open("day18.txt").read().split("\n")
data = []
for r in range(len(raw)):
    data.append([int(raw[r].split()[2][-2:-1]), int(raw[r].split()[2][2:-2],16)])

# 0... R
# 1... D
# 2... L
# 3... U
dirDict = dict()
dirDict[0] = (0,1)
dirDict[1] = (1,0)
dirDict[2] = (0,-1)
dirDict[3] = (-1,0)

nodes = [(0,0)] #earlier attempt, but there is no need to track the nodes/corners
curnode = nodes[0]
border = 0
maxX = 0
for i in range(len(data)): #only really used to find the length of the border and the max value of X axis
    direction = dirDict.get(data[i][0])
    nextnode = (direction[0] * data[i][1] + curnode[0], direction[1] * data[i][1] + curnode[1])
    border += abs(direction[0] * data[i][1]) + abs(direction[1] * data[i][1])
    nodes.append(nextnode)
    if nextnode[1] > maxX:
        maxX = nextnode[1]
    curnode = nextnode

area = 0
curpos = (0,0)
for m in range(len(data)):
    direction = dirDict.get(data[m][0])
    nextpos = (direction[0] * data[m][1] + curpos[0], direction[1] * data[m][1] + curpos[1])
    if data[m][0] == 3: #if we move up, add everything to the right up to maxX to the total area
        area += (maxX - curpos[1])*(data[m][1])
    elif data[m][0] == 1: #if we move down, subtract everything to the right up to maxX from the total area
        area -= (maxX - curpos[1]) * (data[m][1])
    curpos = nextpos

interior = area + 1 - int(border/2) #pick's theorem
print(interior + border)