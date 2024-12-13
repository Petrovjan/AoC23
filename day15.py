data = open("day15.txt").read().split(",")

for i in range(len(data)):
    div = data[i].find("-") + data[i].find("=")
    data[i] = [data[i][:div+1], data[i][div+1:]]

print(data)

def getHash(str):
    cv = 0
    for ch in str:
        cv += ord(ch)
        cv *= 17
        cv = cv%256
    return cv

boxes = dict()

for j in range(len(data)):
    if data[j][1][:1] == "-":
        box = getHash(data[j][0])
        if box in boxes.keys():
            content = boxes.get(box)
        else:
            continue
        for c in range(len(content)):
            if content[c][0] == data[j][0]:
                content.pop(c)
                boxes[box] = content
                break

    elif data[j][1][:1] == "=":
        box = getHash(data[j][0])
        if box in boxes.keys():
            content = boxes.get(box)
            for c in range(len(content)):
                if content[c][0] == data[j][0]:
                    content[c] = [data[j][0], data[j][1][1:]]
                    boxes[box] = content
                    break
            else:
                content.append([data[j][0], data[j][1][1:]])
                boxes[box] = content
        else:
            boxes[box] = [[data[j][0], data[j][1][1:]]]

    else:
        raise RuntimeError

print(boxes)

score = 0
for key,value in boxes.items():
    if value == []:
        continue
    else:
        for v in range(len(value)):
            score += ((key+1) * (v+1) * int(value[v][1]))

print(score)