raw = open("day20.txt").read().split("\n")
print(raw)

flops = dict()
conjs = dict()
br = ()

for mod in raw:
    if "=br" in mod:
        br = tuple([i.strip() for i in mod[mod.find("->")+2:].split(',')])
    elif "%" in mod:
        flops[mod[1:3]] = [0, [i.strip() for i in mod[mod.find("->")+2:].split(',')]]
    elif "&" in mod:
        conjs[mod[1:3]] = [[],[i.strip() for i in mod[mod.find("->")+2:].split(',')]]

for ck, cv in conjs.items():
    for row in raw:
        source = row[1:3]
        targets = [x.strip() for x in row[row.find("->")+2:].split(",")]
        if ck in targets:
            cv[0].append([source, 0])

rounds = 1000
signals = []
lowcount = 0
highcount = 0

def invert(b):
    b_dict = {0: 1, 1: 0}
    return b_dict.get(b)


rounds = 0

rkround = 0
cdround = 0
zfround = 0
qxround = 0

while rkround == 0 or cdround == 0 or zfround == 0 or qxround == 0:
    rounds += 1
    lowcount += 1 #signal to broadcaster
    for b in range(len(br)):
        signals.append(["br", 0, br[b]])
        lowcount += 1
    while len(signals) > 0:
        sig = signals.pop(0)
        dest = sig[2]
        orig = sig[0]
        sig = sig[1]

        if dest in flops.keys():
            flop = flops.get(dest)
            if sig == 1:
                continue
            else:
                flop[0] = invert(flop[0])
                for ftg in flop[1]:
                    signals.append([dest, flop[0], ftg])
                    if flop[0] == 0:
                        lowcount += 1
                    else:
                        highcount += 1
                flops[dest] = flop

        elif dest in conjs.keys():
            conj = conjs.get(dest)
            for c in range(len(conj[0])):
                if orig == conj[0][c][0]:
                    conj[0][c][1] = sig
            pulse = 0
            # if dest == "gh":
            #     print(rounds)
            #     print(conj[0])
            for d in range(len(conj[0])):
                if dest == "gh":
                    if conj[0][d][0] == "rk" and conj[0][d][1] == 1 and rkround == 0:
                        rkround = rounds
                        print("rk", rkround)
                    elif conj[0][d][0] == "cd" and conj[0][d][1] == 1 and cdround == 0:
                        cdround = rounds
                        print("cd", cdround)
                    elif conj[0][d][0] == "zf" and conj[0][d][1] == 1 and zfround == 0:
                        zfround = rounds
                        print("zf",zfround)
                    elif conj[0][d][0] == "qx" and conj[0][d][1] == 1 and qxround == 0:
                        qxround = rounds
                        print("qx",qxround)
                if conj[0][d][1] == 0:
                    pulse = 1
            for ctg in conj[1]:
                signals.append([dest, pulse, ctg])
                if pulse == 0:
                    lowcount += 1
                else:
                    highcount += 1

print(rkround*cdround*zfround*qxround)