time = [45988373]
distance = [295173412781210]

sum = 1
for t in range(len(time)):
    low = (time[t] - (time[t] ** 2 - 4 * distance[t]) ** (1 / 2)) / 2
    high = (time[t] + (time[t] ** 2 - 4 * distance[t]) ** (1 / 2)) / 2
    if high % 1 != 0:
        high = int(high)
    else:
        high = int(high) - 1
    high = int(high)
    low = int(low) + 1
    print(low, high)
    sum *= high - low + 1

print(sum)