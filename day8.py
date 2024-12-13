import math

instr = "LRRLRRRLRRLLLRLLRRLRRLLRRRLRRLLRLRRRLRLRRLRLRRRLRLRLRRLLRLRLRRLRRRLRRRLRRRLRLRRLLLLRLLRLLRRLRRRLLLRLRRRLRLRRRLRLRRLRRRLRRRLRLRLLRRRLLRLLRLRLRLRLLRRLRRLRRRLRRLRLRLRLRLRRLRRRLLRRRLLRLLLRRRLLRRRLRRRLRRLRLRRLRLLRRLLRRLRLRLRRLRLRRLLRRRLLRRRLLRLRRRLRLRRRLRLRRRLRRRLRRLRRLRRLLRRRLRRRLLLRRRR"
raw = open("day8.txt").read().split("\n")
mapa = dict()
starts = []
ends = []
for i in raw:
    if i[2:3] == "A":
        starts.append(i[0:3])
    elif i[2:3] == "Z":
        ends.append(i[0:3])
    mapa[i[0:3]] = [i[7:10],i[12:15]]
print(mapa)

def lcm(lengths):
    lcm = lengths[0]
    done = False
    while not done:
        done = True
        for l in lengths[1:]:
            if lcm%l != 0:
                done = False
                lcm += lengths[0]
                break
    return lcm

def resolve(instr, mapa, place, target):
    steps = 0
    stop = 1000
    while True:
        if stop == 0:
            return None
        stop -= 1
        for i in instr:
            steps += 1
            if i == "L":
                place = mapa.get(place)[0]
            elif i == "R":
                place = mapa.get(place)[1]
            else:
                print("error")
        if place == target:
            return steps

print(starts)
print(ends)

paths = dict()
lengths = []
for s in starts:
    for e in ends:
        r = resolve(instr, mapa, s, e)
        if r is not None:
            paths[s] = [e, r]
            lengths.append(r)
print(lengths)

print(lcm(lengths))


