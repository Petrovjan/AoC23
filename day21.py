import copy

data = open("day21.txt").read().split("\n")
for d in range(len(data)):
    data[d] = [x for x in data[d]]
print(data)

srow = 0
scol = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            srow = i
            scol = j

data[srow][scol] = "."

srow = 0
scol = len(data[0])

odd = dict()
even = dict()
even[(srow,scol)] = 0
possdir = [(-1,0),(0,1),(1,0),(0,-1)]

last = [(srow,scol)]
for r in range(1,197):
    next = copy.deepcopy(last)
    for pos in last:
        next.remove(pos)
        for dir in possdir:
            nfrow = pos[0] + dir[0]
            nfcol = pos[1] + dir[1]
            if (nfrow, nfcol) not in odd.keys() and (nfrow, nfcol) not in even.keys():
                if nfrow >= 0 and nfrow < len(data) and nfcol >= 0 and nfcol < len(data[0]):
                    if data[nfrow][nfcol] == ".":
                        next.append((nfrow, nfcol))
                        if r%2 == 0:
                            even[(nfrow, nfcol)] = r
                        else:
                            odd[(nfrow, nfcol)] = r
    last = next
print(len(even))

# nextDict = dict()
# last = [(srow,scol)]
# for r in range(1,197+131+131+131+131+131):
#     next = copy.deepcopy(last)
#     nextDict.clear()
#     for pos in last:
#         next.remove(pos)
#         for dir in possdir:
#             nfrow = pos[0] + dir[0]
#             nfcol = pos[1] + dir[1]
#             if (nfrow, nfcol) not in odd.keys() and (nfrow, nfcol) not in even.keys() and (nfrow, nfcol) not in nextDict.keys():
#                 if nfrow < 0:
#                     fitnfrow = nfrow + len(data) * (int((abs(nfrow) - 1) / len(data)) + 1)
#                 elif nfrow >= len(data):
#                     fitnfrow = nfrow - len(data) * (int(nfrow / len(data)))
#                 else:
#                     fitnfrow = nfrow
#                 if nfcol < 0:
#                     fitnfcol = nfcol + len(data[0]) * (int((abs(nfcol) - 1) / len(data[0])) + 1)
#                 elif nfcol >= len(data[0]):
#                     fitnfcol = nfcol - len(data[0]) * (int(nfcol / len(data[0])))
#                 else:
#                     fitnfcol = nfcol
#                 if fitnfrow < 0 or fitnfrow >= len(data):
#                     pass
#                 if data[fitnfrow][fitnfcol] in ".S" :
#                     next.append((nfrow, nfcol))
#                     nextDict[(nfrow, nfcol)] = r
#                     if r%2 == 0:
#                         even[(nfrow, nfcol)] = r
#                     else:
#                         odd[(nfrow, nfcol)] = r
#     last = next
# print(len(odd))