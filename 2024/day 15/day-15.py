from functools import cache

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


def is_possible(map_of_scale_warehouse, dots, lbox, rbox, player : tuple, y):
    directions = {'^' : (0,-1), 'v' : (0,1), '<' : (-1,0), '>' : (1,0)}
    inv_directions = {'^' : (0,1), 'v' : (0,-1), '<' : (1,0), '>' : (-1,0)}

    a = addtuple(player, directions[y])

    if a in dots: return True
    if map_of_scale_warehouse[a[1]][a[0]] == '#':
        return False
    
    if y == "^" or y == 'v':
        if a in lbox:
            return is_possible(map_of_scale_warehouse, dots, lbox, rbox, a, y) and is_possible(map_of_scale_warehouse, dots, lbox, rbox, addtuple(a, (1,0)), y)
        elif a in rbox:
            return is_possible(map_of_scale_warehouse, dots, lbox, rbox, a, y) and is_possible(map_of_scale_warehouse, dots, lbox, rbox, addtuple(a, (-1,0)), y)
    
    else:
        if a in lbox:
            return is_possible(map_of_scale_warehouse, dots, lbox, rbox, addtuple(a, (1, 0)), y)
        if a in rbox:
            return is_possible(map_of_scale_warehouse, dots, lbox, rbox, addtuple(a, (-1, 0)), y)


    return False

def move(map_of_scale_warehouse, dots :list, lbox :list, rbox :list, player :tuple, y):
    directions = {'^' : (0,-1), 'v' : (0,1), '<' : (-1,0), '>' : (1,0)}
    inv_directions = {'^' : (0,1), 'v' : (0,-1), '<' : (1,0), '>' : (-1,0)}


    a = addtuple(player, directions[y])
 
    if y == "^" or y == 'v':
        if a in lbox:
            dots, lbox, rbox, p = move(map_of_scale_warehouse, dots, lbox, rbox, a, y)
            dots, lbox, rbox, p = move(map_of_scale_warehouse, dots, lbox, rbox, addtuple(a,directions['>']), y)
        if a in rbox:
            dots, lbox, rbox, p = move(map_of_scale_warehouse, dots, lbox, rbox, a, y)
            dots, lbox, rbox, p = move(map_of_scale_warehouse, dots, lbox, rbox, addtuple(a,directions['<']), y)
    
    else:
        if a in lbox:
            dots, lbox, rbox, p = move(map_of_scale_warehouse, dots, lbox, rbox, a, y)
        if a in rbox:
            dots, lbox, rbox, p = move(map_of_scale_warehouse, dots, lbox, rbox, a, y)


    if a in dots:
        if map_of_scale_warehouse[player[1]][player[0]] == '[':
            lbox.remove(player)
            lbox.append(a)
        if map_of_scale_warehouse[player[1]][player[0]] == ']':
            rbox.remove(player)
            rbox.append(a)
        map_of_scale_warehouse[player[1]][player[0]],  map_of_scale_warehouse[a[1]][a[0]] = map_of_scale_warehouse[a[1]][a[0]],  map_of_scale_warehouse[player[1]][player[0]]
        dots.remove(a)
        dots.append(player)
        player = a

    return dots, lbox, rbox, player

def moveRobot2(map_of_scale_warehouse, dots, lbox, rbox, player, instructions):
    for i, x in enumerate(instructions):
        for j, y in enumerate(x):
            if is_possible(map_of_scale_warehouse, dots, lbox, rbox, player, y):
                dots, lbox, rbox, player = move(map_of_scale_warehouse, dots, lbox, rbox, player, y)

            # print(y)
            # print_grid(map_of_scale_warehouse)
            # print()
            
            #print(player)
            #print(boxs)

    return lbox




def moveRobot(map_of_warehouse, dots, boxs, player, instructions):
    for i, x in enumerate(instructions):
        for j, y in enumerate(x):
            player, boxs, dots = movement(map_of_warehouse, dots, boxs, player, y)
            #print(player)
            #print(boxs)

    return boxs

def print_grid(map_of_scale_warehouse):
    for a in map_of_scale_warehouse:
        print("".join(a))


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

    print("part 1: " + str(sum([100*x[1]+x[0] for x in final_boxs])))

    map_of_scale_warehouse = []
    dots.clear()
    lbox = []
    rbox = []

    for i,x in enumerate(map_of_warehouse):
        line = ''
        for j,y in enumerate(x):
            if y == '#':
                line += "##"
            elif y == '.':
                line += '..'
                dots.append((2*j,i))
                dots.append((2*j + 1,i))
            elif y == 'O':
                line += '[]'
                lbox.append((2*j,i))
                rbox.append((2*j + 1,i))
            else:
                player = (2*j,i)
                dots.append((2*j + 1,i))
                line += "@."

        map_of_scale_warehouse.append(line)

    map_of_scale_warehouse = [list(row) for row in map_of_scale_warehouse]


    print_grid(map_of_scale_warehouse)
    final_boxs = moveRobot2(map_of_scale_warehouse, dots, lbox, rbox, player, instructions)

    print("part 2: " + str(sum([100*x[1]+x[0] for x in final_boxs])))
aoc15()