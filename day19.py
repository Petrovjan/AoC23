import copy

instr = open("day19.txt").read().split("\n\n")[0]
input = open("day19.txt").read().split("\n\n")[1]

instr = instr.split("\n")
input = input.split("\n")

for i in range(len(input)):
    input[i] = input[i].split(",")
    input[i][0] = int(input[i][0][input[i][0].find("=")+1:])
    input[i][1] = int(input[i][1][input[i][1].find("=") + 1:])
    input[i][2] = int(input[i][2][input[i][2].find("=") + 1:])
    input[i][3] = int(input[i][3][input[i][3].find("=") + 1:-1])

insDict = dict()
for j in range(len(instr)):
    instr[j] = instr[j].split(",")
    insVal = []
    for k in range(len(instr[j])):
        if k == 0:
            insVal.append(instr[j][0][instr[j][0].find("{")+1:])
            insKey = str(instr[j][0][:instr[j][0].find("{")])
        elif "}" in instr[j][k]:
            insVal.append(instr[j][k][:-1])
        else:
            insVal.append(instr[j][k])
    insDict[insKey] = tuple(insVal)
print(insDict.items())

#input X,M,A,S

sumX = 0
sumM = 0
sumA = 0
sumS = 0


partDict = dict()
for l in range(len(input)):
    partDict[tuple(input[l])] = "in"
print(partDict.items())

def nextStep(insDict, key, curpos):
    checks = insDict.get(curpos)
    x = key[0]
    m = key[1]
    a = key[2]
    s = key[3]
    for myInstr in checks:
        if ":" in myInstr:
            cond = myInstr[:myInstr.find(":")]
            res = myInstr[myInstr.find(":")+1:]
            if eval(cond):
                return res
            else:
                continue
        else:
            return myInstr
    raise RuntimeError


while len(partDict) != 0:
    newPartDict = copy.deepcopy(partDict)
    for key,val in partDict.items():
        nS = nextStep(insDict, key, val)
        if nS == "A":
            sumX += key[0]
            sumM += key[1]
            sumA += key[2]
            sumS += key[3]
            newPartDict.pop(key)
        elif nS == "R":
            newPartDict.pop(key)
        else:
            newPartDict[key] = nS
    partDict = copy.deepcopy(newPartDict)

print(sumX+sumM+sumA+sumS)
