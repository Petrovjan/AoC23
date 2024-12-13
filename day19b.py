import copy

instr = open("day19.txt").read().split("\n\n")[0]

instr = instr.split("\n")

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

accepted = []
inpDict = dict()
inpDict[((1,4000),(1,4000),(1,4000),(1,4000))] = "in"
print(inpDict.items())

def nextStep(insDict, keyRange, curPos):
    checks = insDict.get(curPos)

    xrange = keyRange[0]
    mrange = keyRange[1]
    arange = keyRange[2]
    srange = keyRange[3]

    newInp = dict()

    for myInstr in checks:
        if ":" in myInstr:
            if ">" in myInstr[:myInstr.find(":")]:
                num = int(myInstr[myInstr.find(">") + 1:myInstr.find(":")])
                newPos = myInstr[myInstr.find(":") + 1:]
                if "x" in myInstr[:myInstr.find(":")]:
                    if num >= xrange[1]:
                        stayKeyRange = (xrange,mrange,arange,srange)
                        moveKeyRange = ()
                    elif num < xrange[0]:
                        moveKeyRange = (xrange,mrange,arange,srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = ((xrange[0], num), mrange, arange, srange)
                        moveKeyRange = ((num+1, xrange[1]), mrange, arange, srange)

                elif "m" in myInstr[:myInstr.find(":")]:
                    if num >= mrange[1]:
                        stayKeyRange = (xrange,mrange,arange,srange)
                        moveKeyRange = ()
                    elif num < mrange[0]:
                        moveKeyRange = (xrange,mrange,arange,srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = (xrange, (mrange[0], num), arange, srange)
                        moveKeyRange = (xrange, (num+1, mrange[1]), arange, srange)

                elif "a" in myInstr[:myInstr.find(":")]:
                    if num >= arange[1]:
                        stayKeyRange = (xrange, mrange, arange, srange)
                        moveKeyRange = ()
                    elif num < arange[0]:
                        moveKeyRange = (xrange, mrange, arange, srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = (xrange, mrange, (arange[0], num), srange)
                        moveKeyRange = (xrange, mrange, (num + 1, arange[1]), srange)

                elif "s" in myInstr[:myInstr.find(":")]:
                    if num >= srange[1]:
                        stayKeyRange = (xrange, mrange, arange, srange)
                        moveKeyRange = ()
                    elif num < srange[0]:
                        moveKeyRange = (xrange, mrange, arange, srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = (xrange, mrange, arange, (srange[0], num))
                        moveKeyRange = (xrange, mrange, arange, (num + 1, srange[1]))

            else:
                num = int(myInstr[myInstr.find("<") + 1:myInstr.find(":")])
                newPos = myInstr[myInstr.find(":") + 1:]
                if "x" in myInstr[:myInstr.find(":")]:
                    if num <= xrange[0]:
                        stayKeyRange = (xrange,mrange,arange,srange)
                        moveKeyRange = ()
                    elif num > xrange[1]:
                        moveKeyRange = (xrange,mrange,arange,srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = ((num, xrange[1]), mrange, arange, srange)
                        moveKeyRange = ((xrange[0], num - 1), mrange, arange, srange)

                elif "m" in myInstr[:myInstr.find(":")]:
                    if num >= mrange[1]:
                        stayKeyRange = (xrange,mrange,arange,srange)
                        moveKeyRange = ()
                    elif num < mrange[0]:
                        moveKeyRange = (xrange,mrange,arange,srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = (xrange, (num, mrange[1]), arange, srange)
                        moveKeyRange = (xrange, (mrange[0], num - 1), arange, srange)

                elif "a" in myInstr[:myInstr.find(":")]:
                    if num >= arange[1]:
                        stayKeyRange = (xrange, mrange, arange, srange)
                        moveKeyRange = ()
                    elif num < arange[0]:
                        moveKeyRange = (xrange, mrange, arange, srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = (xrange, mrange, (num, arange[1]), srange)
                        moveKeyRange = (xrange, mrange, (arange[0], num - 1), srange)

                elif "s" in myInstr[:myInstr.find(":")]:
                    if num >= srange[1]:
                        stayKeyRange = (xrange, mrange, arange, srange)
                        moveKeyRange = ()
                    elif num < srange[0]:
                        moveKeyRange = (xrange, mrange, arange, srange)
                        stayKeyRange = ()
                    else:
                        stayKeyRange = (xrange, mrange, arange, (num, srange[1]))
                        moveKeyRange = (xrange, mrange, arange, (srange[0], num - 1))
        else:
            newPos = myInstr
            moveKeyRange = (xrange, mrange, arange, srange)
            stayKeyRange = ()

        if len(moveKeyRange) != 0:
            newInp[moveKeyRange] = newPos

        if len(stayKeyRange) == 0:
            break
            print("breaking")
        else:
            xrange = stayKeyRange[0]
            mrange = stayKeyRange[1]
            arange = stayKeyRange[2]
            srange = stayKeyRange[3]
    return newInp

while len(inpDict) != 0:
    newInpDict = copy.deepcopy(inpDict)
    for key,val in inpDict.items():
        newInpDict.pop(key)
        newSplit = nextStep(insDict, key, val)
        checkedSplit = copy.deepcopy(newSplit)
        for skey,sval in newSplit.items():
            if sval == "A":
                accepted.append(skey)
                checkedSplit.pop(skey)
            elif sval == "R":
                checkedSplit.pop(skey)
            elif key == ():
                pass
        newInpDict = newInpDict | checkedSplit
    inpDict = newInpDict

print(accepted)


result = 0
for y in range(len(accepted)):
    poss = 1
    for x in range(len(accepted[y])):
        poss *= (accepted[y][x][1] - accepted[y][x][0] + 1)
    result += poss
print(result)