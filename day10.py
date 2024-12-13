import copy

raw = open("day10.txt").read().split("\n")
print(raw)

sRow = 0
sCol = 0

for i in range(len(raw)):
    for j in range(len(raw[i])):
        if raw[i][j] == "S":
            sRow = i
            sCol = j

print(sRow, sCol)

positions = dict()

#positions[(sRow,sCol)] = ""



def solve(positions, raw, sRow, sCol):
    for dir in [[0,-1],[0,1],[1,0],[-1,0]]:
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
    step = 1
    while True:
        step += 1
        newpos = dict()
        for curpos,prevdir in positions.items():
            cursign = raw[curpos[0]][curpos[1]]
            if raw[curpos[0]][curpos[1]] == "|" and prevdir[0] == -1: #going up
                if (curpos[0] - 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] - 1, curpos[1])] = (-1, 0)
            elif raw[curpos[0]][curpos[1]] == "|" and prevdir[0] == 1: #going down
                if (curpos[0] + 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] + 1, curpos[1])] = (1, 0)

            elif raw[curpos[0]][curpos[1]] == "-" and prevdir[1] == -1:  # going left
                if (curpos[0], curpos[1] - 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] - 1)] = (0, -1)
            elif raw[curpos[0]][curpos[1]] == "-" and prevdir[1] == 1:  # going right
                if (curpos[0], curpos[1] + 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] + 1)] = (0, 1)

            elif raw[curpos[0]][curpos[1]] == "L" and prevdir == (0,-1):  # came left, goes up
                if (curpos[0] - 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] - 1, curpos[1])] = (-1, 0)
            elif raw[curpos[0]][curpos[1]] == "L" and prevdir == (1,0):  # came down, goes right
                if (curpos[0], curpos[1] + 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] + 1)] = (0, 1)

            elif raw[curpos[0]][curpos[1]] == "J" and prevdir == (0,1):  # came right, goes up
                if (curpos[0] - 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] - 1, curpos[1])] = (-1, 0)
            elif raw[curpos[0]][curpos[1]] == "J" and prevdir == (1,0):  # came down, goes left
                if (curpos[0], curpos[1] - 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] - 1)] = (0, -1)

            elif raw[curpos[0]][curpos[1]] == "7" and prevdir == (0,1):  # came right, goes down
                if (curpos[0] + 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] + 1, curpos[1])] = (1, 0)
            elif raw[curpos[0]][curpos[1]] == "7" and prevdir == (-1,0):  # came up, goes left
                if (curpos[0], curpos[1] - 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] - 1)] = (0, -1)

            elif raw[curpos[0]][curpos[1]] == "F" and prevdir == (0,-1):  # came left, goes down
                if (curpos[0] + 1, curpos[1]) in newpos.keys():
                    return step
                newpos[(curpos[0] + 1, curpos[1])] = (1, 0)
            elif raw[curpos[0]][curpos[1]] == "F" and prevdir == (-1,0):  # came up, goes right
                if (curpos[0], curpos[1] + 1) in newpos.keys():
                    return step
                newpos[(curpos[0], curpos[1] + 1)] = (0, 1)

            else:
                print("error")

        positions = copy.deepcopy(newpos)


print(solve(positions, raw, sRow, sCol))