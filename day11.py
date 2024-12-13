data = open("day11.txt").read().split("\n")

for i in range(len(data)):
    data[i] = [*data[i]]

for j in range(len(data)-1,-1,-1):
    if "#" not in data[j]:
        data[j] = ["H" for x in range(len(data[j]))]

for l in range(len(data[0])-1,-1,-1):
    empty = True
    for k in range(len(data)):
        if data[k][l] == "#":
            empty = False
    if empty:
        for k in range(len(data)):
            data[k][l] = "H"

galaxies = []
for m in range(len(data)):
    for n in range(len(data[m])):
        if data[m][n] == "#":
            galaxies.append([m,n])

distDict = dict()

expand = 1000000

for start in galaxies:
    for end in galaxies:
        if start == end:
            continue
        else:
            hscore = 0
            if start[1] != end[1]:
                hpath = data[start[0]][min(start[1],end[1])+1:max(start[1],end[1])]
                hscore = len(hpath) + hpath.count("H")*(expand-1)+1
            vpath = []
            vscore = 0
            if start[0] != end[0]:
                for r in range(min(start[0],end[0])+1,max(start[0],end[0])):
                    vpath.append(data[r][end[1]])
                vscore = len(vpath) + vpath.count("H")*(expand-1)+1
            if start[0] < end[0]:
                distDict[(start[0], start[1], end[0], end[1])] = hscore + vscore
            elif start[0] == end[0] and start[1] < end[1]:
                distDict[(start[0], start[1], end[0], end[1])] = hscore + vscore
            else:
                distDict[(end[0], end[1], start[0], start[1])] = hscore + vscore

print(sum(distDict.values()))