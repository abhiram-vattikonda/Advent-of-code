
def calcpath(data, currentPos, val, reachablePeak) -> int:
    height = len(data)
    width = len(data[0])
    sum = 0
    if val == 9:
        reachablePeak.add(currentPos)
        return 1, 1
    
    if currentPos[0] + 1 < width and int(data[currentPos[1]][currentPos[0] + 1]) == val + 1:
        w, a = calcpath(data, (currentPos[0] + 1, currentPos[1]), val + 1, reachablePeak)
        sum += a

    if currentPos[0] - 1 >= 0 and int(data[currentPos[1]][currentPos[0] - 1]) == val + 1:
        w, a = calcpath(data, (currentPos[0] - 1, currentPos[1]), val + 1, reachablePeak)
        sum += a

    if currentPos[1] + 1 < height and int(data[currentPos[1] + 1][currentPos[0]]) == val + 1:
        w, a = calcpath(data, (currentPos[0], currentPos[1] + 1), val + 1, reachablePeak)
        sum += a

    if currentPos[1] - 1 >= 0 and int(data[currentPos[1] - 1][currentPos[0]]) == val + 1:
        w, a = calcpath(data, (currentPos[0], currentPos[1] - 1), val + 1, reachablePeak)
        sum += a

    return len(reachablePeak), sum

def aoc10():
    file = open("puzzle10.txt", 'r')
    data = []
    with open('puzzle10.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    
    totalpeaks = 0
    totalpaths = 0
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            if int(x) == 0:
                peaks, paths = calcpath(data, (j, i), 0, set({}))
                totalpeaks += peaks
                totalpaths += paths

    print(totalpeaks)
    print(totalpaths)

aoc10()