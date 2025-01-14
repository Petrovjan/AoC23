import copy

raw = open("day10.txt").read().split("\n")

data = [[]]
dr = 0
for r in range(len(raw)): #extending the field to see the previously hidden gaps
    data.extend([[],[],[]])
    for c in range(len(raw[r])):
        if raw[r][c] == "S":
            data[dr].extend([".",".","."])
            data[dr+1].extend(["-","S","-"])
            data[dr+2].extend([".",".","."])
        elif raw[r][c] == ".":
            data[dr].extend([".",".","."])
            data[dr+1].extend([".",".","."])
            data[dr+2].extend([".",".","."])
        elif raw[r][c] == "|":
            data[dr  ].extend([".","|","."])
            data[dr+1].extend([".","|","."])
            data[dr+2].extend([".","|","."])
        elif raw[r][c] == "-":
            data[dr  ].extend([".",".","."])
            data[dr+1].extend(["-","-","-"])
            data[dr+2].extend([".",".","."])
        elif raw[r][c] == "L":
            data[dr  ].extend([".","|","."])
            data[dr+1].extend([".","L","-"])
            data[dr+2].extend([".",".","."])
        elif raw[r][c] == "J":
            data[dr  ].extend([".","|","."])
            data[dr+1].extend(["-","J","."])
            data[dr+2].extend([".",".","."])
        elif raw[r][c] == "7":
            data[dr  ].extend([".",".","."])
            data[dr+1].extend(["-","7","."])
            data[dr+2].extend([".","|","."])
        elif raw[r][c] == "F":
            data[dr  ].extend([".",".","."])
            data[dr+1].extend([".","F","-"])
            data[dr+2].extend([".","|","."])
        else:
            print("error extending field")
    dr += 3

raw = data #variable names are a mess due to changes in the code between p1 and p2

sRow = 0
sCol = 0

for i in range(len(raw)):
    for j in range(len(raw[i])):
        if raw[i][j] == "S":
            sRow = i
            sCol = j

positions = dict()
visited = dict()

def solve(positions, raw, sRow, sCol):
    global visited
    visited[(sRow, sCol)] = "S"
    for dir in [[0,-1],[0,1],[1,0],[-1,0]]: #finding available directions from the start point
        next = raw[sRow + dir[0]][sCol + dir[1]]
        if next == "|" and dir[1] == 0:
            pass
        elif next == "-" and dir[0] == 0:
            pass
        elif next == "L" and dir in [[0,-1], [1,0]]:
            pass
        elif next == "J" and dir in [[0,1], [1,0]]:
            pass
        elif next == "7" and dir in [[0, 1], [-1, 0]]:
            pass
        elif next == "F" and dir in [[0, -1], [-1, 0]]:
            pass
        else:
            continue
        positions[(sRow + dir[0], sCol + dir[1])] = (dir[0], dir[1])
        visited[(sRow + dir[0], sCol + dir[1])] = next
    step = 1
    while True: #going in the available directions until the paths both have the same cell as their next step. Fortunately there are no dead ends and the two paths meet exactly on a single cell.
        step += 1
        newpos = dict()
        for curpos,prevdir in positions.items():
            cursign = raw[curpos[0]][curpos[1]]
            if cursign == "|" and prevdir[0] == -1: #going up
                if (curpos[0] - 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] - 1, curpos[1])] = (-1, 0)
                visited[(curpos[0] - 1, curpos[1])] = raw[curpos[0]][curpos[1]]
            elif cursign == "|" and prevdir[0] == 1: #going down
                if (curpos[0] + 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] + 1, curpos[1])] = (1, 0)
                visited[(curpos[0] + 1, curpos[1])] = raw[curpos[0]][curpos[1]]

            elif cursign == "-" and prevdir[1] == -1:  # going left
                if (curpos[0], curpos[1] - 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] - 1)] = (0, -1)
                visited[(curpos[0], curpos[1] - 1)] = raw[curpos[0]][curpos[1]]
            elif cursign == "-" and prevdir[1] == 1:  # going right
                if (curpos[0], curpos[1] + 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] + 1)] = (0, 1)
                visited[(curpos[0], curpos[1] + 1)] = raw[curpos[0]][curpos[1]]

            elif cursign == "L" and prevdir == (0,-1):  # came left, goes up
                if (curpos[0] - 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] - 1, curpos[1])] = (-1, 0)
                visited[(curpos[0] - 1, curpos[1])] = raw[curpos[0]][curpos[1]]
            elif cursign == "L" and prevdir == (1,0):  # came down, goes right
                if (curpos[0], curpos[1] + 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] + 1)] = (0, 1)
                visited[(curpos[0], curpos[1] + 1)] = raw[curpos[0]][curpos[1]]

            elif cursign == "J" and prevdir == (0,1):  # came right, goes up
                if (curpos[0] - 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] - 1, curpos[1])] = (-1, 0)
                visited[(curpos[0] - 1, curpos[1])] = raw[curpos[0]][curpos[1]]
            elif cursign == "J" and prevdir == (1,0):  # came down, goes left
                if (curpos[0], curpos[1] - 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] - 1)] = (0, -1)
                visited[(curpos[0], curpos[1] - 1)] = raw[curpos[0]][curpos[1]]

            elif cursign == "7" and prevdir == (0,1):  # came right, goes down
                if (curpos[0] + 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] + 1, curpos[1])] = (1, 0)
                visited[(curpos[0] + 1, curpos[1])] = raw[curpos[0]][curpos[1]]
            elif cursign == "7" and prevdir == (-1,0):  # came up, goes left
                if (curpos[0], curpos[1] - 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] - 1)] = (0, -1)
                visited[(curpos[0], curpos[1] - 1)] = raw[curpos[0]][curpos[1]]

            elif cursign == "F" and prevdir == (0,-1):  # came left, goes down
                if (curpos[0] + 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] + 1, curpos[1])] = (1, 0)
                visited[(curpos[0] + 1, curpos[1])] = raw[curpos[0]][curpos[1]]
            elif cursign == "F" and prevdir == (-1,0):  # came up, goes right
                if (curpos[0], curpos[1] + 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] + 1)] = (0, 1)
                visited[(curpos[0], curpos[1] + 1)] = raw[curpos[0]][curpos[1]]

            else:
                print("error")

        positions = copy.deepcopy(newpos)


print("part1: ",int(solve(positions, raw, sRow, sCol)/3)) #divided by three because each pipe is now three times as long

for key in visited:
    raw[key[0]][key[1]] = "X"

raw[0][0] = "V"
outside = [[0,0]]
while len(outside) != 0:
    o = outside.pop()
    try:
        for dir in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            next = raw[o[0] + dir[0]][o[1] + dir[1]]
            if raw[o[0]][o[1]] == "V" and next != "V" and next != "X":
                raw[o[0] + dir[0]][o[1] + dir[1]] = "V"
                outside.append([o[0] + dir[0],o[1] + dir[1]])
                changed = True
            else:
                continue
    except IndexError:
        pass

for m in range(len(raw)): #replace all cells next to the loop by "W", since we don't want them in the result - they originally didn't exist
    for n in range(len(raw[m])):
        try:
            for dir in [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]:
                bla = (m + dir[0], n + dir[1])
                if (m + dir[0], n + dir[1]) in visited.keys():
                    if raw[m][n] not in "XV":
                        raw[m][n] = "W"
        except IndexError:
            pass

result = 0
for o in range(len(raw)):
    for p in range(len(raw[o])):
        if raw[o][p] not in "WXV":
            result += 1

print("part2: ",int(result/9))