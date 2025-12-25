import time
start_time = time.time()

with open("inp9.txt") as f:
    lines = f.read().splitlines()

lines = [tuple(map(int, line.split(","))) for line in lines]

# PART 1
m = 0
for i,line in enumerate(lines):
    for j in lines[i:]:
        area = abs(line[0] - j[0] + 1) * abs(line[1] - j[1] + 1)
        if area > m:
            m = area
print(m)
print(f"----- {time.time() - start_time} -----")

# PART 2
def area(line1 :tuple[int, int], line2 :tuple[int, int]):
    return (abs(line1[0]-line2[0])+1) * (abs(line1[1]-line2[1]) + 1)

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


def print_grid(rows :int, columns :int, points :list[tuple]):
    for j in range(rows):
        for i in range(columns):
            if (i, j) in points:
                print("#", end='')
            else:
                print(".", end='')
        print()

    
def rec_fill(inside_point :tuple[int, int], grid :list[list[int]]):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    
    stack = [inside_point]
    new_points = []

    while stack:
        p = stack.pop()

        if not (0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid)):
            continue

        if grid[p[1]][p[0]] == 1:
            continue

        new_points.append(p)
        grid[p[1]][p[0]] = 1
        
        for direction in directions:
            new_point = (p[0] + direction[0], p[1] + direction[1])
            stack.append(new_point)

    return new_points, grid

allx, ally = [], []
for a, b in lines:
    allx.append(a)
    ally.append(b)

unqx = sorted(set(allx))
unqy = sorted(set(ally))
mapx = {x : i for i, x in enumerate(unqx)}
mapy = {y : i for i, y in enumerate(unqy)}

compressed_points = [(mapx[a], mapy[b]) for a,b in lines]

# boundry points
points = []
l = len(compressed_points)
for i in range(l):
   points.extend(add_btw_points(compressed_points[i % l], compressed_points[(i + 1) % l]))
points = list(set(points))


grid = [[1 if (j, i) in points else 0 for j in range(len(unqx))] for i in range(len(unqy))]
print(f"{len(grid)}x{len(grid[0])}")
print("Boundry")

# ray casting
inside = (-1, -1)
for j in range(len(unqy)):
    for i in range(len(unqx)):
        if (i, j) in points:
            continue

        fence_c = 0 # no of #'s
        for k in range(i, len(unqx)):
            if (k, j) in points:

                if ((k-1, j) not in points or (k+1, j) not in points):
                    fence_c += 1
                
        
        if fence_c and fence_c % 2 != 0:
            inside = (i, j)
            break
    
    if inside != (-1, -1):
        break

print("raytrace")

# print_grid(len(unqx), len(unqy), points)
print(inside)
new_points, grid = rec_fill(inside, grid)
points.extend(new_points)
# print_grid(len(unqx), len(unqy), points)
print("fill")

# Calc max area
mapx = {mapx[a] : a for a in mapx}
mapy = {mapy[a] : a for a in mapy}
b_area = 0
fin_points = (a, b)

for a in compressed_points:
    for b in compressed_points:
        cona = (mapx[a[0]], mapy[a[1]])
        conb = (mapx[b[0]], mapy[b[1]])

        k = area(cona, conb)
        if k > b_area and grid[b[1]][a[0]] and grid[a[1]][b[0]]:
            hole = False
            for w in range(min(a[1], b[1]), max(a[1], b[1])):
                for q in range(min(a[0], b[0]), max(a[0], b[0])):
                    if not grid[w][q]:
                        hole = True
                        break
                if hole:
                    break
            if hole:
                continue
            b_area = max(b_area, k)
            fin_points = (cona, conb)
            ma, mb = a, b

print((ma, mb))
print(fin_points)
print("Part 2: ", area(fin_points[0], fin_points[1]))

# 176819620 is too low
# 1603403500 is wrong
# 4600046948 is too high

print(f"----- {time.time() - start_time} -----")