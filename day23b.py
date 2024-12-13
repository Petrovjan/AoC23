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

for f in range(len(field[len(field) - 2])):
    if field[len(field) - 2][f] == ".":
        frow = len(field) - 2
        fcol = f

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def intersect(lst1, lst2):
    try:
        if len(list(set(lst1) & set(lst2))) > 0:
            return True
        else:
            return False
    except:
        print(lst1, lst2)


xroads = dict()
xrc = 1
xroads[(srow,scol)] = (0,[[1,0]])
for u in range(len(field)):
    for v in range(len(field[u])):
        if field[u][v] == ".":
            nbs = []
            for xdir in dirs:
                if field[u + xdir[0]][v + xdir[1]] in ".<>^v":
                    nbs.append(xdir)
            if len(nbs) > 2:
                xroads[(u,v)] = (xrc,nbs)
                xrc += 1
xroads[(frow,fcol)]= (100,[[-1,0]])

def findJunctions(xkey, xval, field, xroads, dirs):
    junc = dict()
    for juncdir in xval[1]:
        steps = 1
        jpos = [xkey[0] + juncdir[0], xkey[1] + juncdir[1]]
        jvisited = dict()
        jvisited[(xkey[0],xkey[1])] = 1
        notfound = True
        while notfound:
            steps += 1
            for jdir in dirs:
                if field[jpos[0] + jdir[0]][jpos[1] + jdir[1]] == "#":
                    continue
                elif (jpos[0] + jdir[0],jpos[1] + jdir[1]) in jvisited.keys():
                    continue
                elif (jpos[0] + jdir[0],jpos[1] + jdir[1]) in xroads.keys():
                    tarval = xroads.get((jpos[0] + jdir[0],jpos[1] + jdir[1]))
                    junc[(xval[0],tarval[0])] = steps
                    notfound = False
                    break
                else:
                    jvisited[(jpos[0], jpos[1])] = steps
                    jpos = [jpos[0] + jdir[0],jpos[1] + jdir[1]]
                    break
    return junc



junctions = dict()
for xkey,xval in xroads.items():
    possjunc = findJunctions(xkey, xval, field, xroads, dirs)
    for pkey, pval in possjunc.items():
        if pkey in junctions.keys():
            continue
        # elif (pkey[2], pkey[3], pkey[0], pkey[1]) in junctions.keys():
        #     continue
        else:
            junctions[pkey] = pval

print(junctions)

trips = dict()
for jkey, jval in junctions.items():
    if jkey[0] in trips.keys():
        trip = copy.deepcopy(trips.get(jkey[0]))
        trip.append((jkey[1],jval))
        trips[jkey[0]] = trip[:]
    else:
        trips[jkey[0]] = [(jkey[1],jval)]

print(trips)

def myFunc(e):
  return e[2]

# visited = dict()  #dict of dicts
steps = [(0,[],0)] #current juntion, visited, length
finished = []
bestlen = 0
while len(steps) > 0:
    nextsteps = []
    steps.sort(reverse=True, key=lambda e: e[2])
    step = steps[0]
    possteps = trips.get(step[0])
    for ps in range(len(possteps)):
        if possteps[ps][0] not in step[1]:
            newlen = step[2] + possteps[ps][1]
            visited = copy.deepcopy(step[1])
            visited.append(step[0])
            if possteps[ps][0] == 100:
                if newlen > bestlen:
                    bestlen = newlen
                    print("target len",newlen)
                finished.append((visited,newlen))
            nextsteps.append((possteps[ps][0],visited,newlen))
    steps.pop(0)
    steps = nextsteps + steps
