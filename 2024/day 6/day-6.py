import time
start_time = time.time()

with open("puzzle6.txt") as f:
    lines = f.read().split()

rows = len(lines)
columns = len(lines[0])

walls = []
start = (0, 0)
for y in range(rows):
    for x in range(columns):
        if lines[y][x] == '#':
            walls.append((x, y))

        if lines[y][x] == '^':
            start = (x, y)

print(rows, columns)
def rotate_right(vector :tuple[int, int]):
    return (-vector[1], vector[0])

def calc_newpos(curr :tuple[int, int], direction :tuple[int, int], opp_direction :bool = False):
    if opp_direction:
        return (curr[0] - direction[0], curr[1] - direction[1])

    return (curr[0] + direction[0], curr[1] + direction[1])

def find_path(walls :list[tuple[int, int]], currpos :tuple[int, int], rows :int, columns :int, direction :str):
    walls_encountered = []
    visited = [currpos]
    wall_hit_dir_dict :dict[tuple[int, int], list] = {}
    newpos = calc_newpos(currpos, direction)

    while 0 <= newpos[0] < columns and 0 <= newpos [1] < rows:
        
        visited.append(newpos)
        newpos = calc_newpos(newpos, direction)

        if 0 < newpos[0] >= columns or 0 < newpos[1] >= rows:
            break

        if newpos in walls:
            walls_encountered.append(newpos)
            if wall_hit_dir_dict.get(direction):
                if newpos in wall_hit_dir_dict[direction]:
                    return [], []

                wall_hit_dir_dict[direction].append(newpos)
            else:
                wall_hit_dir_dict[direction] = [newpos]

            newpos = calc_newpos(newpos, direction, True)
            direction = rotate_right(direction)

    return visited, walls_encountered
    


visited, walls_hit = find_path(walls, start, rows, columns, (0, -1))
print(len(visited))
print("part 1:", len(set(visited)))   
print(f"----- {time.time() - start_time} -----")


loop_blocks = []
default_path = visited.copy()
for y in range(rows):
    for x in range(columns):
        if (x, y) not in default_path:
            continue
        new_walls = walls.copy()
        new_walls.append((x, y))

        visited, hits = find_path(new_walls, start, rows, columns, (0, -1))
        
        if visited == []:
            loop_blocks.append((x, y))


print("part 2:", len(loop_blocks))
# new_wall_loc = []
# direction = (0, -1)
# for i in range(len(walls_hit) - 2):
#     wall_is_blocking_loop = False
#     if direction == (0, -1):
#         new_wall = (walls_hit[i][0] - 1, walls_hit[i+2][1] - 1)
#     if direction == (0, 1):
#         new_wall = (walls_hit[i][0] + 1, walls_hit[i+2][1] + 1)
#     if direction == (-1, 0):
#         new_wall = (walls_hit[i+2][0] - 1, walls_hit[i][1] + 1)
#     if direction == (1, 0):
#         new_wall = (walls_hit[i+2][0] + 1, walls_hit[i][1] - 1)

#     if new_wall != start and new_wall not in new_wall_loc and new_wall not in walls:
#         currpos = calc_newpos(walls_hit[i+2], direction)
#         while currpos != new_wall:
#             if currpos in walls:
#                 wall_is_blocking_loop = True

#             currpos = calc_newpos(currpos, rotate_right(rotate_right(rotate_right(direction))))

#         if not wall_is_blocking_loop:
#             new_wall_loc.append(new_wall)
    
#     direction = rotate_right(direction)

# print(new_wall_loc)
# print("part 2:", len(new_wall_loc))

print(f"----- {time.time() - start_time} -----")
