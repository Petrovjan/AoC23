import copy

raw = open("day23.txt").read().split("\n")
field = []
for i in range(len(raw)):
    field.append([x for x in raw[i]])

print(field)

padding = ["#" for y in range(len(field[0]))]
field.insert(0, padding)
field.insert(len(field), padding)

for s in range(len(field[1])):
    if field[1][s] == ".":
        srow = 1
        scol = s

for f in range(len(field[len(field)-2])):
    if field[len(field)-2][f] == ".":
        frow = len(field)-2
        fcol = f

visited = dict() #(1,2):[0,1,2]
paths = [[srow,scol,[0]]]

dirs = [[-1,0],[0,1],[1,0],[0,-1]]

def intersect(lst1, lst2):
    try:
        if len(list(set(lst1) & set(lst2))) > 0:
            return True
        else:
            return False
    except:
        print(lst1, lst2)

print(field[134][137])

finished = []
pathcounter = 0
while len(paths) > 0:
    newpaths = []
    for path in paths:
        poss = []
        if path[0] == frow and path[1] == fcol:
            finished.append(path[2])
            continue
        for dir in dirs:
            if field[path[0]+dir[0]][path[1]+dir[1]] == "#":
                continue
            elif field[path[0]+dir[0]][path[1]+dir[1]] == "v" and dir == [-1,0]:
                continue
            elif field[path[0]+dir[0]][path[1]+dir[1]] == "^" and dir == [1,0]:
                continue
            elif field[path[0]+dir[0]][path[1]+dir[1]] == ">" and dir == [0,-1]:
                continue
            elif field[path[0]+dir[0]][path[1]+dir[1]] == "<" and dir == [0,1]:
                continue
            elif (path[0]+dir[0], path[1]+dir[1]) in visited.keys() and intersect(path[2], visited.get((path[0]+dir[0], path[1]+dir[1]))):
                continue
            elif path[0] == 134 and path[1] == 137 and dir[0] != 1 and dir[1] != 0:
                continue
            else:
                poss.append([path[0]+dir[0], path[1]+dir[1], path[2]])

        if len(poss) == 1:
            newpaths.append(poss[0])
        elif len(poss) > 1:
            for n in range(len(poss)):
                pathcounter += 1
                a = copy.deepcopy(poss[n][2])
                a.append(pathcounter)
                newpaths.append([poss[n][0], poss[n][1], a[:]])

        if (path[0], path[1]) in visited.keys():
            oldp = visited.get((path[0], path[1]))
            oldp = copy.deepcopy(oldp)
            oldp.append(path[2][-1])
            visited[(path[0], path[1])] = oldp[:]
        else:
            visited[(path[0], path[1])] = [path[2][-1]]

    paths = copy.deepcopy(newpaths)

print(finished)

pathlens = dict()
for pval in visited.values():
    for p in pval:
        if p in pathlens.keys():
            pathlens[p] = pathlens.get(p) + 1
        else:
            pathlens[p] = 1

totallens = []
for fin in finished:
    tl = 0
    for t in range(len(fin)):
        tl += pathlens.get(fin[t])
    totallens.append(tl)

print(totallens)
print(max(totallens))