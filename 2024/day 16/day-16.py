import heapq

def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def rotate_right(x :tuple[int, int]):
    return (-x[1], x[0])

def rotate_left(x :tuple[int, int]):
    return (x[1], -x[0])

   
    
def bfs(player, points, walls, direction, forward, turns):

    return forward, turns



def aoc16():
    points = []
    walls = []
    data = []

    with open("puzzle16.txt", 'r') as file:
        for line in file:
            data.append(line)

    height = len(data)
    width = len(data[0]) - 1

    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == '.':
                points.append((i, j))
            elif y == '#':
                walls.append((i, j))
            elif y == 'E':
                end = (i, j)
            elif y == 'S':
                player = (i, j)

    print(height, width) 

    forward, turns = bfs(player, points, walls, (0, -1), 0, 0)


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

aoc16()