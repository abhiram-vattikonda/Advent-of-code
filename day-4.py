
def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def hasXmas(data, currentPos, localPos, direction) -> bool:
    if localPos == 3:
        return True
    
    height = len(data)
    width = len(data[0]) - 1
    values = ['X', 'M', 'A', 'S']


    a = addtuple(currentPos, direction)
    if 0 <= a[0] < width and 0 <= a[1] < height:
        if data[a[1]][a[0]] == values[localPos+1]:
            return hasXmas(data, a, localPos+1, direction)

    return False


def aoc4():
    data = []
    with open("puzzle4.txt", 'r') as file:
        for line in file:
            data.append(line)
    
    directions = [(1,0), (1,1), (0,1), (-1,1), (-1, 0), (-1,-1), (0,-1), (1, -1)]

    num_of_xmax = 0
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y != 'X':
                continue

            for direction in directions:
                if hasXmas(data, (j, i), 0, direction):
                    num_of_xmax += 1
                    #print(f"from {(j, i)} in {direction} direction with totatl {num_of_xmax}")
                    
        

    print(num_of_xmax)

    
aoc4()