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

result = 0
remdata = copy.deepcopy(data)
dot = 0
for first in data:
    remdata.pop(0)
    for second in remdata:
        if first == second:
            print("identical checks!")
            continue
        else:
            result += willMeet(first,second)
print(result)