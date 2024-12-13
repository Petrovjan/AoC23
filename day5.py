import copy

seeds = [432986705,28073546,1364097901,88338513,2733524843,234912494,3151642679,224376393,485709676,344068331,
         1560394266,911616092,3819746175,87998136,892394515,435690182,4218056486,23868437,848725444,8940450]
seedst = [79,14,55,13]
raw = open("day5.txt").read().split("\n\n")
data = [x.split("\n") for x in raw]
maps = []

for y in data:
    tmap = []
    for z in range(1, len(y)):
        tmap.append(y[z].split())
    maps.append(tmap)

for a in range(len(maps)):
    for b in range(len(maps[a])):
        for c in range(len(maps[a][b])):
            maps[a][b][c] = int(maps[a][b][c])

minloc = 0
for seed in seeds:
    target = seed
    for d in range(len(maps)):
        for e in range(len(maps[d])):
            dbg = maps[d][e]
            if target >= maps[d][e][1] and target < (maps[d][e][1] + maps[d][e][2]):
                target = target - maps[d][e][1] + maps[d][e][0]
                break
    if minloc == 0 or target < minloc:
        minloc = target
print(minloc)

#############

def inRange(slice, map):
    if map[1] <= slice[1]+slice[2] and map[1]+map[2] >= slice[0]+slice[2]:
        return True
    return False

def split(slice, map):
    res = []
    if slice == [79, 92, -5]:
        pass
    maprange = [map[1], map[1]+map[2]-1]
    slcierange = [slice[0] + slice[2],slice[1]+slice[2]]
    lowrange = min(slice[0] + slice[2], maprange[0])
    if lowrange != maprange[0]:
        res.append([lowrange-slice[2], maprange[0]-slice[2]-1, slice[2]])
    res.append([max(slice[0] + slice[2], maprange[0])-slice[2], min(slice[1] + slice[2], maprange[1])-slice[2], slice[2] + map[0] - map[1]])
    toprange = max(slice[1] + slice[2], maprange[1])
    if toprange != maprange[1]:
        res.append([maprange[1]+1-slice[2],toprange-slice[2],slice[2]])
    return res

#change 4 times
slices = []
for s in range(0,len(seeds),2):
    slices.append([seeds[s], seeds[s]+seeds[s+1]-1, 0])

for d in range(len(maps)):
    newslices = []
    for slice in slices:
        upd = False
        for e in range(len(maps[d])):
            if inRange(slice, maps[d][e]):
                newslices += split(slice, maps[d][e])
                upd = True
                #TODO - bug, slices can be duplicated if there are two valid maps for one slice
        if not upd:
            newslices.append(slice)
    slices = copy.deepcopy(newslices)

result = 0
for s in slices:
    if s[0]+s[2] < result or result == 0:
        result = s[0]+s[2]
print(result)