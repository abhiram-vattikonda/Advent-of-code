import time
start_time = time.time()

with open("test.txt") as f:
    lines = f.read().splitlines()

lines = [tuple(map(int, line.split(","))) for line in lines]

# PART 1
# m = 0
# for i,line in enumerate(lines):
#     for j in lines[i:]:
#         area = abs(line[0] - j[0] + 1) * abs(line[1] - j[1] + 1)
#         if area > m:
#             m = area
# print(m)

# PART 2
def area(line1, line2):
    return abs(line1[0]-line2[0] + 1) * abs(line1[1]-line2[1] + 1)

def add_btw_points(l1, l2):
    new_points = []
    if l1[0] == l2[0]:
        x = l1[0]
        y1 = l1[1]
        y2 = l2[1]

        start = min(y1, y2)
        end = max(y1, y2)

        new_points.extend((x, k) for k in range(start, end + 1))


    if l1[1] == l2[1]:
        y = l1[1]
        x1 = l1[0]
        x2 = l2[0]

        start = min(x1, x2)
        end = max(x1, x2)

        new_points.extend((k, y) for k in range(start, end + 1))

    return new_points

 
points = []
l = len(lines)
for i in range(l):
   points.extend(add_btw_points(lines[i % l], lines[(i + 1) % l]))
points = list(set(points))
print("Boundry")

# points = sorted(points)
# print(points)
def print_grid(grid):
    for i in grid:
        print(i)
        
max_x = max([x for x, y in lines]) + 3
max_y = max([y for x, y in lines]) + 3
grid = ['.'*(max_x)]*max_y
for i in range(max_y):
    # print(i)
    for j in range(max_x):
        if (j, i) in lines:
            grid[i] = f"{grid[i][:j]}#{grid[i][j+1:]}"

for x, y in points:
    if (x, y) not in lines:
        grid[y] = f"{grid[y][:x]}X{grid[y][x+1:]}"

borders = grid.copy()


all_points_x = points.copy()
for y in range(max_y):
    white = True
    for x in range(max_x):
        if white and grid[y][x] == 'X':
            white = False
        elif not white and grid[y][x] == 'X':
            white = True
        
        if not white and grid[y][x] == '.':
            grid[y] = f"{grid[y][:x]}X{grid[y][x+1:]}"
            all_points_x.append((x, y))


grid = borders.copy()
all_points_y = points.copy()
for x in range(max_x):
    white = True
    for y in range(max_y):
        if white and grid[y][x] == 'X':
            white = False
        elif not white and grid[y][x] == 'X':
            white = True
        
        if not white and grid[y][x] == '.':
            grid[y] = f"{grid[y][:x]}X{grid[y][x+1:]}"
            all_points_y.append((x, y))

print_grid(grid)

all_points = [a for a in all_points_y if a in all_points_x]

grid = ['.'*(max_x)]*max_y
for y in range(max_y):
    for x in range(max_x):
        if (x, y) in all_points:
            grid[y] = f"{grid[y][:x]}X{grid[y][x+1:]}"

print_grid(grid)


# all_points = []
# for i, p1 in enumerate(points):
#     print(i)
#     for j, p2 in enumerate(points[i+1:]):
#         all_points.extend(add_btw_points(p1, p2))
#     all_points = list(set(all_points))
#     print("\b", time.time() - start_time) 

# m = 0
# for i, p1 in enumerate(lines):
#     print(i)
#     for j, p2 in enumerate(lines[i+1:]):
#         c1 = (p1[0], p2[1])
#         c2 = (p2[0], p1[1])
#         if c1 in all_points and c2 in all_points:
#             m = max(m, abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1))   
#     print("\b", time.time() - start_time) 
# print(m)
print(f"----- {time.time() - start_time} -----")