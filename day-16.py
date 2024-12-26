

def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def find_path(player, char, end, dots, walls, directions, scores):
    scores = []

    

    return 

def aoc16():
    map = []

    with open("puzzle16.txt", 'r') as file:
        for line in file:
            map.append(line)

    dots = []
    walls = []
    for i,x in enumerate(map):
        for j, y in enumerate(x):
            if y == '#'
                walls.append((j, i))
            if y == '.'
                dots.append((j, i))
            if y == 'S':
                player = (j, i)
            if y == 'E':
                end = (j, i)

    char = '>'
    directions = {'^' : (0,-1), 'v' : (0,1), '<' : (-1,0), '>' : (1,0)}

    find_path(player, char, end, dots, walls, directions, 0)



aoc16()