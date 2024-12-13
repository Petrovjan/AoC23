import copy

raw = open("day17.txt").read().split("\n")
data = []
for i in range(len(raw)):
    data.append([int(x) for x in raw[i]])

data.append([0 for y in range(len(data[0]))])
data.insert(0, [0 for y in range(len(data[0]))])
for i in range(len(data)):
    data[i].append(0)
    data[i].insert(0, 0)
print(data)

next = dict()
next[(1, 1, 6, "S")] = [0 , [0]]
visited = dict()

goal = (len(data) - 2, len(data[0]) - 2)
print("goal: ", goal)

# goal = (1,9)

def solve(data, next, visited, goal):
    while True:
        nextstep = min(next, key=next.get)   #(1,1,2,"R") - row, col, steps left, dir
        nextheat = next[nextstep]
        next.pop(nextstep)
        addtonext = dict()
        possdir = [("U",-1,0),("R",0,1),("D",1,0),("L",0,-1)]
        if nextstep[3] == "R":
            possdir.pop(3)
        elif nextstep[3] == "L":
            possdir.pop(1)
        elif nextstep[3] == "U":
            possdir.pop(2)
        elif nextstep[3] == "D":
            possdir.pop(0)
        for d in possdir:
            nkey = (nextstep[0] + d[1], nextstep[1] + d[2], (0 + (1 + nextstep[2]) * nextstep[3].count(d[0])), d[0])
            heat = data[nkey[0]][nkey[1]]
            if heat == 0:
                continue
            elif nkey in visited.keys():
                continue
            elif nkey[2] > 9:
                continue
            elif nkey[2] == 0 and nextstep[2] < 3:
                continue
            elif nkey in next.keys() and next[nkey][0] < (nextheat[0] + heat):
                continue
            else:
                newheat = copy.deepcopy(nextheat)
                newheat[0] += heat
                newheat[1].append([heat, nkey[0],nkey[1]])
                addtonext[nkey] = newheat
                if (nkey[0],nkey[1]) == goal and nkey[2] >= 3:
                    print(nkey)
                    print(newheat)
                    return newheat[0]
        visited[nextstep] = nextheat
        next = next | addtonext

print(solve(data, next, visited, goal))