
def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def multuple(a:tuple, i:int):
    return tuple(x * i for x in a)

def hasX_max(data, currentPos):

    height = len(data)
    width = len(data[0]) - 1
    d1 = False
    d2 = False
    a = addtuple(currentPos, (-1, -1))
    b = addtuple(currentPos, (1, 1))
    x = addtuple(currentPos, (-1, 1))
    y = addtuple(currentPos, (1, -1))

    if 0 <= a[0] < width and 0 <= a[1] < height and 0 <= b[0] < width and 0 <= b[1] < height and 0 <= x[0] < width and 0 <= x[1] < height and 0 <= y[0] < width and 0 <= y[1] < height:
        if (data[a[1]][a[0]] == "M" and data[b[1]][b[0]] == 'S') or (data[a[1]][a[0]] == "S" and data[b[1]][b[0]] == 'M'):
            d1 = True
        if (data[x[1]][x[0]] == "M" and data[y[1]][y[0]] == 'S') or (data[x[1]][x[0]] == "S" and data[y[1]][y[0]] == 'M'):
            d2 = True
    
    return d1 and d2

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
    with open("test.txt", 'r') as file:
        for line in file:
            data.append(line)
    
    directions = [(1,0), (1,1), (0,1), (-1,1), (-1, 0), (-1,-1), (0,-1), (1, -1)]

    num_of_xmax = 0
    num_of_x_max = 0
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == 'X':
                for direction in directions:
                    if hasXmas(data, (j, i), 0, direction):
                        num_of_xmax += 1
                        #print(f"from {(j, i)} in {direction} direction with totatl {num_of_xmax}")

            elif y == 'A':
                if hasX_max(data, (j, i)):
                    num_of_x_max += 1   

                
                    
        

    print(num_of_xmax)
    print(num_of_x_max)

    
aoc4()