import copy
raw = open("day13.txt").read().split("\n\n")
data = [x.split("\n") for x in raw]
print(data)

cdata = copy.deepcopy(data)

fdata = []
for k in range(len(cdata)):
    for i in range(len(cdata[k])):
        for j in range(len(cdata[k][i])):
            if len(fdata) <= k:
                fdata.append([cdata[k][i][j]])
            elif len(fdata[k]) <= j:
                fdata[k].append(cdata[k][i][j])
            else:
                a = fdata[k][j][:]
                b = cdata[k][i][j]
                fdata[k][j] = fdata[k][j][:] + cdata[k][i][j]
print(fdata)

def countDiff(fstr, sstr):
    count = 0
    for i in range(len(fstr)):
        if fstr[i] != sstr[i]:
            count += 1
    return count

def confirmMatch(field, cand):
    i = 0
    diffs = 0
    while cand - i >= 0 and cand + i + 1 < len(field):
        diffs += countDiff(field[cand-i], field[cand+i+1])
        i += 1
    if diffs == 1:
        return True
    else:
        return False


result = 0
for s in range(len(data)):
    for c in range(len(fdata[s])-1):
        if countDiff(fdata[s][c], fdata[s][c + 1]) <= 1:
            if confirmMatch(fdata[s], c):
                result += c + 1
                break
            else:
                continue
    else:
        for r in range(len(data[s])-1):
            if countDiff(data[s][r], data[s][r + 1]) <= 1:
                if confirmMatch(data[s], r):
                    result += (r + 1)*100
                    break
                else:
                    continue
print("part2: ",result)

