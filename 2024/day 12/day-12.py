

def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def fencecost(data :list, currentPos :tuple, visited :set):
    visited.add(currentPos)
    #print(currentPos)
    height = len(data)
    width =len(data[0])
    plot = data[currentPos[1]][currentPos[0]]

    perimeter = 0
    area = 0

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for direction in directions:
        a = addtuple(currentPos, direction)
        if a not in visited:
            if 0 <= a[0] < width and 0 <= a[1] < height and data[a[1]][a[0]] == plot:
                ar, per, visited = fencecost(data, a, visited)
                area += ar
                perimeter += per
            else:
                perimeter += 1
        elif data[a[1]][a[0]] != plot:
            perimeter += 1
    
    return area + 1, perimeter, visited



def fencecost2(data :list, currentPos :tuple, visited :set):
    visited.add(currentPos)
    #print(currentPos)
    height = len(data)
    width =len(data[0])
    plot = data[currentPos[1]][currentPos[0]]

    corners = 0
    area = 0

    cornerchecks = [[(1,0), (1,1), (0,1)], [(-1,0), (-1,1), (0,1)], [(-1,0), (-1,-1), (0,-1)], [(1,0), (1,-1), (0,-1)]]

    for sets in cornerchecks:
        a = addtuple(currentPos, sets[0])
        b = addtuple(currentPos, sets[1])
        c = addtuple(currentPos, sets[2])

        if 0 <= a[0] < width and 0 <= a[1] < height and 0 <= b[0] < width and 0 <= b[1] < height and 0 <= c[0] < width and 0 <= c[1] < height:
            if data[a[1]][a[0]] != plot and data[b[1]][b[0]] != plot and data[c[1]][c[0]] != plot:
                corners +=1
            elif data[a[1]][a[0]] == plot and data[b[1]][b[0]] != plot and data[c[1]][c[0]] == plot:
                corners += 1
            elif data[a[1]][a[0]] != plot and data[b[1]][b[0]] == plot and data[c[1]][c[0]] != plot:
                corners += 1
        else:
            if (0 > a[0] or a[0] >= width or 0 > a[1] or a[1] >= height) and (0 > b[0] or b[0] >= width or 0 > b[1] or b[1] >= height) and (0 > c[0] or c[0] >= width or 0 > c[1] or c[1] >= height):
                corners += 1
            elif (0 > a[0] or a[0]  >= width or 0 > a[1] or a[1]  >= height) and (0 > b[0] or b[0]  >= width or 0 > b[1] or b[1] >= height) and (0 <= c[0] < width and 0 <= c[1] < height) and data[c[1]][c[0]] != plot:
                corners += 1
            elif (0 <= a[0] < width and 0 <= a[1] < height ) and (0 > b[0] or b[0]  >= width or 0 > b[1] or b[1]  >= height) and (0 > c[0] or c[0]  >= width or 0 > c[1] or c[1]  >= height) and data[a[1]][a[0]] != plot:
                corners += 1

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for direction in directions:
        a = addtuple(currentPos, direction)
        if a not in visited:
            if 0 <= a[0] < width and 0 <= a[1] < height and data[a[1]][a[0]] == plot:
                ar, cor, visited = fencecost2(data, a, visited)
                area += ar
                corners += cor
    
    return area + 1, corners, visited






def aoc12():
    data = []
    with open('puzzle12.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    total1 = 0
    visited = set({})
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if (j, i) in visited:
                continue

            area, perimeter, visits = fencecost(data, (j,i), visited)

            visited = visits
            total1 += area * perimeter




            #print(f"End of Area for {y}. Cost is {area * perimeter} with {area} and {perimeter}")

    print(f"Part 1: {total1}")

    total2 = 0
    visited.clear()
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if (j, i) in visited:
                continue

            area, corners, visits = fencecost2(data, (j,i), visited)

            visited = visits
            total2 += area * corners




    print(f"Part 2: {total2}")

aoc12()
