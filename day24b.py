import copy

data = open("day24.txt").read().split("\n")
data = [x.split(", ") for x in data]

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
print(data)


def willMeet(first, second):
    low = 200000000000000
    high = 400000000000000

    a = 1
    b = (-1 * first[3]) / first[4]
    c = (first[3] * first[1]) / first[4] - first[0]

    d = 1
    e = (-1 * second[3]) / second[4]
    f = (second[3] * second[1]) / second[4] - second[0]

    if b-e == 0:
        return False

    intX = -1*f - (e*(f-c))/(b-e)
    intY = (f - c)/(b - e)
    tA = (intY - first[1])/first[4]
    tB = (intY - second[1])/second[4]
    pass

    if intX >= low and intX <= high and tA > 0:
        if intY >= low and intY <= high and tB > 0:
            return True
    return False

# result = 0
# remdata = copy.deepcopy(data)
# dot = 0
# for first in data:
#     remdata.pop(0)
#     for second in remdata:
#         if first == second:
#             print("identical checks!")
#             continue
#         else:
#             result += willMeet(first,second)
# print(result)


velDict = dict()
for point in data:
    vel = point[3]
    if vel in velDict.keys():
        oldval = copy.deepcopy(velDict.get(vel))
        oldval.append(point[0])
        velDict[vel] = oldval
    else:
        velDict[vel] = [point[0]]

duplVelDict = dict()
for key,val in velDict.items():
    if len(val) > 1:
        duplVelDict[key] = val

print(duplVelDict)

broken = False
for possvel in range(-3000, 3000):
    if possvel == 0:
        continue
    if broken:
        broken = False
        continue
    for dkey, dval in duplVelDict.items():
        if broken:
            break
        for i in range(len(dval)-1):
            dist = abs(dval[i] - dval[i+1])
            velocity = possvel - dkey
            if velocity == 0:
                broken = True
                break
            a = dist%velocity
            if dist%velocity != 0:
                broken = True
                break
    if not broken:
        print(possvel)
    if broken:
        broken = False
        continue

xvel = 148
yvel = 159
zvel = 249


# ft = [241284760156765, 213633705299964, 273986496029776, 57, 97, 8]
# st = [247734440322603, 211037541638632, 425633703630138, 57, 109, -223]
# tt = [277557227178647, 478655596305920, 329087019719498, 57, -167, 53]

ft = [241284760156765, 273986496029776, 213633705299964, 57-148, 8-249, 97-159]
st = [84607269180419,102095256416750 ,31310497114262 , 352-148, 339-249, 438-159]
tt = [93328649189759, 26248115804612, 49995133784360, 290-148, 377-159, 390-249]

# timeFtoS = (st[0] - ft[0])/(148-57)
# timeStoT = (tt[0] - st[0])/(148-57)

print(willMeet(ft, st))

rx = 194723518367339
ry = 181910661443432
rz = 150675954587450
print(rx+ry+rz)