raw = open("day7.txt").read().split("\n")
data = [x.split() for x in raw]

def isFive(hand):
    if hand.count(hand[0]) == 5:
        return True
    return False

five = []
four = []
fullhouse = []
three = []
twopairs = []
onepair = []
nothing = []

def handValue(hand):
    tripleV = ""
    doubleV = ""
    for h in hand:
        j = hand.count("J")
        if h == "J":
            if j == 5:
                return 6
            else:
                continue
        c = hand.count(h)
        if c + j == 5:
            return 6
        elif c + j == 4:
            return 5
        elif c == 3:
            if tripleV.count(h) == 0:
                tripleV += h
        elif c == 2:
            if doubleV.count(h) == 0:
                doubleV += h
    if len(tripleV) == 1 and len(doubleV) == 1 and j == 0:
        return 4
    elif len(doubleV) == 2 and j == 1:
        return 4
    elif len(tripleV) == 1:
        return 3
    elif len(doubleV) == 1 and j == 1:
        return 3
    elif j == 2:
        return 3
    elif len(doubleV) == 2:
        return 2
    elif len(doubleV) == 1:
        return 1
    elif j == 1:
        return 1
    else:
        return 0

for d in range(len(data)):
    if handValue(data[d][0]) == 6:
        five.append(data[d])
    elif handValue(data[d][0]) == 5:
        four.append(data[d])
    elif handValue(data[d][0]) == 4:
        fullhouse.append(data[d])
    elif handValue(data[d][0]) == 3:
        three.append(data[d])
    elif handValue(data[d][0]) == 2:
        twopairs.append(data[d])
    elif handValue(data[d][0]) == 1:
        onepair.append(data[d])
    else:
        nothing.append(data[d])

def prepare(cardlist):
    for i in range(len(cardlist)):
        if cardlist[i][1] == "684":
            x = cardlist[i]
            pass
        cardlist[i][0] = cardlist[i][0].replace("J", "1")
        cardlist[i][0] = cardlist[i][0].replace("Q", "C")
        cardlist[i][0] = cardlist[i][0].replace("K", "D")
        cardlist[i][0] = cardlist[i][0].replace("A", "E")
        cardlist[i][0] = cardlist[i][0].replace("T", "A")
        cardlist[i][0] = int(cardlist[i][0],16)
    return cardlist

five = prepare(five)
four = prepare(four)
fullhouse = prepare(fullhouse)
three = prepare(three)
twopairs = prepare(twopairs)
onepair = prepare(onepair)
nothing = prepare(nothing)

five.sort(reverse=True)
four.sort(reverse=True)
fullhouse.sort(reverse=True)
three.sort(reverse=True)
twopairs.sort(reverse=True)
onepair.sort(reverse=True)
nothing.sort(reverse=True)

results = [1,0]
#counter, result

def finish(category, results):
    newresult = results
    for i in range(len(category)-1,-1,-1):
        score = int(category[i][1])
        newresult[1] += newresult[0] * score
        newresult[0] += 1
    return newresult

results = finish(nothing,results)
results = finish(onepair,results)
results = finish(twopairs,results)
results = finish(three,results)
results = finish(fullhouse,results)
results = finish(four,results)
results = finish(five,results)

print(results[1])