from functools import cache
import copy

raw = open("day12.txt").read().split("\n")
data = [x.split() for x in raw]

for q in range(len(data)):
    ogf = data[q][0]
    ogb = data[q][1]
    for e in range(4):
        data[q][0] = data[q][0] + "?" + ogf
        data[q][1] = data[q][1] + "," + ogb
# print(data)

springs = []
for d in data:
    springs.append([list(filter(None, d[0].split("."))),d[1].split(",")])
# print(springs)

@cache
def validate(ver, broken):
    if broken == (1,2,2,1):
        pass
    ver = list(ver)
    fullver = ""
    for v in ver:
        fullver = fullver + v + "."
    fullver = fullver[:-1]
    newver = []
    newver.extend(list(filter(None, fullver.split("."))))


    if len(newver) == len(broken):
        sumqm = 0
        for o in range(len(newver)):
            sumqm += newver[o].count("?")
        if newver[0].count("?") == 0 and newver[0].count("#") != broken[0]:
            return False
        for i in range(len(newver)):
            if newver[i].count("?") + newver[i].count("#") >= broken[i] and newver[i].count("#") <= broken[i]:
                continue
            else:
                if sumqm > 0:
                    return True
                else:
                    return False
        return True
    elif len(newver) > len(broken):
        b = 0
        n = 0
        sumqm = 0
        for p in range(len(newver)):
            sumqm += newver[p].count("?")
        if sumqm == 0:
            return False
        while b <= len(broken)-1 and n <= len(newver)-1:
            if newver[n].count("#") > broken[b] and newver[n].count("?") == 0:
                return False
            elif newver[n].count("#") + newver[n].count("?") < broken[b] and newver[n].count("#") > 0 and sumqm < broken[b]:
                return False
            elif newver[n].count("#") + newver[n].count("?") < broken[b] and newver[n].count("#") == 0:
                newver.pop(n)
                newver = tuple(newver)
                return validate(newver, broken)
            else:
                b += 1
                n += 1
        return True
    else:
        sumcross = 0
        sumqm = 0
        for j in range(len(newver)):
            sumcross += newver[j].count("#")
            sumqm += newver[j].count("?")
        if sumcross > sum(broken):
            return False
        elif sumcross + sumqm + len(newver) < sum(broken) + len(broken):
            return False
        else:
            return True


@cache
def firstQOptions(field, broken):
    field = list(field)
    res = 0
    fi = 0
    cha = 0
    found = False
    for f in range(len(field)):
        for ch in range(len(field[f])):
            if field[f][ch] == "?":
                fi = f
                cha = ch
                found = True
                break
        if found:
            break
    else:
        return 1

    verOne = copy.deepcopy(field)
    verOne[fi] = verOne[fi][:cha] + "." + verOne[fi][cha+1:]
    verTwo = copy.deepcopy(field)
    verTwo[fi] = verTwo[fi][:cha] + "#" + verTwo[fi][cha+1:]

    verOne = tuple(verOne)
    verTwo = tuple (verTwo)
    if validate(verOne, broken):
        res += firstQOptions(verOne, broken)
    if validate(verTwo, broken):
        res += firstQOptions(verTwo, broken)

    return res

partone = 0
for m in range(len(springs)):
    field = tuple(springs[m][0])
    broken = springs[m][1]
    for b in range(len(broken)):
        broken[b] = int(broken[b])
    broken = tuple(springs[m][1])
    score = firstQOptions(field, broken)
    print(field,broken, score)
    partone += score
print(partone)