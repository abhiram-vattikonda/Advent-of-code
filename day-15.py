

def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def movement(map_of_warehouse, dots :list, boxs : list, player : tuple, y):
    directions = {'^' : (0,-1), 'v' : (0,1), '<' : (-1,0), '>' : (1,0)}
    inv_directions = {'^' : (0,1), 'v' : (0,-1), '<' : (1,0), '>' : (-1,0)}

    a = addtuple(player, directions[y])

    while a not in dots:
        if map_of_warehouse[a[1]][a[0]] == '#':
            return player, boxs, dots
        
        a = addtuple(a, directions[y])
        
    while addtuple(a, inv_directions[y]) in boxs:
        boxs.append(a)
        dots.remove(a)
        a = addtuple(a, inv_directions[y])
        boxs.remove(a)
        dots.append(a)
        
    dots.append(player)
    player = addtuple(player, directions[y])
    dots.remove(player)
    return player, boxs, dots




def printmap(map_of_warehouse, boxs):
    print(*[x + '\n' for x in map_of_warehouse])

def moveRobot(map_of_warehouse, dots, boxs, player, instructions):
    for i, x in enumerate(instructions):
        for j, y in enumerate(x):
            player, boxs, dots = movement(map_of_warehouse, dots, boxs, player, y)
            #print(player)
            #print(boxs)

    return boxs



def aoc15():
    map_of_warehouse  = []
    instructions = []
    boxs = []
    dots =[]
    ismap = True

    with open("puzzle15.txt", 'r') as file:
        for line in file:
            if ismap:
                if line == '\n':
                    ismap = False
                    continue
                map_of_warehouse.append(line[:-1])

            else:
                instructions.append(line[:-1])

    for i, x in enumerate(map_of_warehouse):
        for j, y in enumerate(x):
            if y == 'O':
                boxs.append((j, i))
            if y == '@':
                player = (j, i)
            if y == '.':
                dots.append((j, i))

    final_boxs = moveRobot(map_of_warehouse, dots, boxs, player, instructions)

    print(sum([100*x[1]+x[0] for x in final_boxs]))

aoc15()