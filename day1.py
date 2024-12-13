raw = open("day1.txt").read().split("\n")
coords = []
for com in raw:
    first = ""
    last = ""
    for i in range(len(com)):
        if com[i].isdigit():
            first = com[i]
            break
    for j in range(len(com)-1,-1,-1):
        if com[j].isdigit():
            last = com[j]
            break
    coordstr = first+last
    coord = int(coordstr)
    coords.append(coord)
print("part1: ", sum(coords))

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

coords = []
for com in raw:
    firstpos = 100
    firstdigitpos = 100
    lastpos = -1
    lastdigitpos = -1
    coordstr = None
    coord = None
    first = None
    last = None
    firstnum = None
    lastnum = None

    for num in range(len(numbers)):
        search = numbers[num]
        x = com.find(search)
        if 0 <= x < firstpos:
            firstpos = x
            firstnum = num + 1

    for i in range(len(com)):
        if com[i].isdigit():
            firstdigit = com[i]
            firstdigitpos = i
            break

    if firstpos > firstdigitpos:
        first = firstdigit
    else:
        first = firstnum

    for num in range(len(numbers)):
        y = com.rfind(numbers[num])
        if y > lastpos:
            lastpos = y
            lastnum = num + 1

    for j in range(len(com)-1,-1,-1):
        if com[j].isdigit():
            lastdigit = com[j]
            lastdigitpos = j
            break

    if lastpos > lastdigitpos:
        last = lastnum
    else:
        last = lastdigit

    coordstr = str(first)+str(last)
    coord = int(coordstr)
    coords.append(coord)

print("part2: ", sum(coords))