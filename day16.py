import functools
from functools import cache

data = open("day16.txt").read().split("\n")
for i in range(len(data)):
    data[i] = tuple([x for x in data[i]])
data = tuple(data)
print(data)

def moveBeam(onebeam, data):
    if onebeam[2] == "U":
        try:
            if onebeam[0] - 1 < 0 or onebeam[1] < 0:
                return None
            next = data[onebeam[0] - 1][onebeam[1]]
            if next == "." or next == "|":
                return [[onebeam[0] - 1, onebeam[1], "U"]]
            elif next == "/":
                return [[onebeam[0] - 1, onebeam[1], "R"]]
            elif next == "!":
                return [[onebeam[0] - 1, onebeam[1], "L"]]
            elif next == "-":
                return [[onebeam[0] - 1, onebeam[1], "L"],[onebeam[0] - 1, onebeam[1], "R"]]
            else:
                raise RuntimeError
        except IndexError:
            return None
    elif onebeam[2] == "R":
        try:
            if onebeam[0] < 0 or onebeam[1] + 1 < 0:
                return None
            next = data[onebeam[0]][onebeam[1] + 1]
            if next == "." or next == "-":
                return [[onebeam[0], onebeam[1] + 1, "R"]]
            elif next == "/":
                return [[onebeam[0], onebeam[1] + 1, "U"]]
            elif next == "!":
                return [[onebeam[0], onebeam[1] + 1, "D"]]
            elif next == "|":
                return [[onebeam[0], onebeam[1] + 1, "U"],[onebeam[0], onebeam[1] + 1, "D"]]
            else:
                raise RuntimeError
        except IndexError:
            return None
    elif onebeam[2] == "D":
        try:
            if onebeam[0] + 1 < 0 or onebeam[1] < 0:
                return None
            next = data[onebeam[0] + 1][onebeam[1]]
            if next == "." or next == "|":
                return [[onebeam[0] + 1, onebeam[1], "D"]]
            elif next == "/":
                return [[onebeam[0] + 1, onebeam[1], "L"]]
            elif next == "!":
                return [[onebeam[0] + 1, onebeam[1], "R"]]
            elif next == "-":
                return [[onebeam[0] + 1, onebeam[1], "L"],[onebeam[0] + 1, onebeam[1], "R"]]
            else:
                raise RuntimeError
        except IndexError:
            return None
    elif onebeam[2] == "L":
        try:
            if onebeam[0] < 0 or onebeam[1] - 1 < 0:
                return None
            next = data[onebeam[0]][onebeam[1] - 1]
            if next == "." or next == "-":
                return [[onebeam[0], onebeam[1] - 1, "L"]]
            elif next == "/":
                return [[onebeam[0], onebeam[1] - 1, "D"]]
            elif next == "!":
                return [[onebeam[0], onebeam[1] - 1, "U"]]
            elif next == "|":
                return [[onebeam[0], onebeam[1] - 1, "U"],[onebeam[0], onebeam[1] - 1, "D"]]
            else:
                raise RuntimeError
        except IndexError:
            return None


possbeams = []
for j in range(len(data)):
    if data[j][0] == "!":
        possbeams.append([j, 0, "D"])
    elif data[j][0] == "." or data[j][0] == "-":
        possbeams.append([j, 0, "R"])
    elif data[j][0] == "|":
        possbeams.append([j, 0, "U"])
        possbeams.append([j, 0, "D"])
    elif data[j][0] == "/":
        possbeams.append([j, 0, "U"])

    if data[j][len(data[j])-1] == "!":
        possbeams.append([j, len(data[j])-1, "U"])
    elif data[j][len(data[j])-1] == "|":
        possbeams.append([j, len(data[j])-1, "U"])
        possbeams.append([j, len(data[j])-1, "D"])
    elif data[j][len(data[j])-1] == "/":
        possbeams.append([j, len(data[j])-1, "D"])
    elif data[j][len(data[j])-1] == "." or data[j][len(data[j])-1] == "-":
        possbeams.append([j, len(data[j])-1, "L"])

for l in range(len(data[0])):
    if data[0][l] == "!":
        possbeams.append([0, l, "R"])
    elif data[0][l] == "." or data[0][l] == "|":
        possbeams.append([0, l, "D"])
    elif data[0][l] == "-":
        possbeams.append([0, l, "R"])
        possbeams.append([0, l, "L"])
    elif data[0][l] == "/":
        possbeams.append([0, l, "L"])

    if data[len(data)-1][l] == "!":
        possbeams.append([len(data)-1, l, "L"])
    elif data[len(data)-1][l] == "-":
        possbeams.append([len(data)-1, l, "R"])
        possbeams.append([len(data)-1, l, "L"])
    elif data[len(data)-1][l] == "/":
        possbeams.append([len(data)-1, l, "R"])
    elif data[len(data)-1][l] == "." or data[len(data)-1][l] == "|":
        possbeams.append([len(data)-1, l, "U"])

print(possbeams)



beam = [[0,0, "D"]]

maxscore = 0
for pb in possbeams:
    beam = [pb]

    energized = dict()
    energized[(beam[0][0],beam[0][1])] = 1

    dupl = dict()
    dupl[tuple(beam[0])] = 1


    while len(beam) > 0:
        firstbeam = tuple(beam.pop())
        newbeams = moveBeam(firstbeam, data)
        if newbeams:
            for newbeam in newbeams:
                if (newbeam[0],newbeam[1]) in energized.keys():
                    curstr = energized.get((newbeam[0],newbeam[1]))
                    energized[(newbeam[0],newbeam[1])] = curstr + 1
                else:
                    energized[(newbeam[0], newbeam[1])] = 1
                if tuple(newbeam) in dupl.keys():
                    continue
                else:
                    dupl[tuple(newbeam)] = 1
                    beam.append(newbeam)
    score = len(energized.keys())
    if score > maxscore:
        maxscore = score
        print(maxscore)
        print(possbeams.index(pb), len(possbeams))


print(maxscore)