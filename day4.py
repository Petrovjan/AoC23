raw = open("day4.txt").read().split("\n")
data = [x.split("|") for x in [y.split(":")[1] for y in raw]]

cards = []
for i in range(len(data)):
    cards.append([data[i][0].split(),data[i][1].split()])

totalscore = 0
for j in range(len(cards)):
    gamescore = 0.5
    for draw in cards[j][0]:
        if draw in cards[j][1]:
            gamescore *= 2
    if gamescore != 0.5:
        totalscore += int(gamescore)

print("part1: ", totalscore)

cardlist = []
for k in range(len(cards)):
    cardlist.append(1)

for j in range(len(cards)):
    a = 0
    for draw in cards[j][0]:
        if draw in cards[j][1]:
            if j + a + 1 >= len(cardlist):
                break
            a += 1
            cardlist[j + a] += 1*cardlist[j]

print(sum(cardlist))