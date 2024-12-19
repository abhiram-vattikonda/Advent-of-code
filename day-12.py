

def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def fencecost(data :list, currentPos :tuple, visited :set):
    visited.add(currentPos)
    print(currentPos)
    height = len(data)
    width =len(data[0])
    plot = data[currentPos[1]][currentPos[0]]

    perimeter = 0
    area = 0

    a = addtuple(currentPos, (1,0))
    if a not in visited:
        if a[0] < width and data[a[1]][a[0]] == plot:
            ar, per, visited = fencecost(data, a, visited)
            area += ar
            perimeter += per
        else:
            perimeter += 1

    a = addtuple(currentPos, (-1,0))
    if a not in visited:
        if a[0] >= 0 and data[a[1]][a[0]] == plot:
            ar, per, visited = fencecost(data, a, visited)
            area += ar
            perimeter += per
        else:
            perimeter += 1

    a = addtuple(currentPos, (0,1))
    if a not in visited:
        if a[1] < height and data[a[1]][a[0]] == plot:
            ar, per, visited = fencecost(data, a, visited)
            area += ar
            perimeter += per
        else:
            perimeter += 1

    a = addtuple(currentPos, (0,-1))
    if a not in visited:
        if a[1] >= 0 and data[a[1]][a[0]] == plot:
            ar, per, visited = fencecost(data, a, visited)
            area += ar
            perimeter += per
        else:
            perimeter += 1

    
    return area + 1, perimeter, visited






def aoc12():
    data = []
    with open('puzzle12.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    total = 0
    visited = set({})
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if (j, i) in visited:
                continue

            area, perimeter, visits = fencecost(data, (j,i), visited)

            visited = visits
            total += area * perimeter

            break




    print(total)

aoc12()
