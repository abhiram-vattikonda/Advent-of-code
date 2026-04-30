import time
from functools import cache

start_time = time.time()

with open("puzzle18.txt", "r") as file:
    data = file.readlines()

data = [tuple(map(int, x.split(','))) for x in data]

l = 70
byte = 1024

blocks = data[:byte]

def addtuple(a :tuple[int], b :tuple[int]):
    return (a[0]+b[0], a[1]+b[1])

visited = []

@cache
def search(pos, end, steps):
    
    # vis = visited.copy()
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    if pos == end:
        # print(f"Steps: {steps}")
        return steps

    if pos in blocks:
        return float("infinity")
    
    if 0 > pos[0] or pos[0] > l or 0 > pos[1] or pos[1] > l:
        return float("infinity")
    
    if pos in visited:
        return float("infinity")

    visited.append(pos)

    v1 = search(addtuple(pos, direction[0]), end, steps+1)
    v2 = search(addtuple(pos, direction[1]), end, steps+1)
    v3 = search(addtuple(pos, direction[2]), end, steps+1)
    v4 = search(addtuple(pos, direction[3]), end, steps+1)

    v = min(v1, v2, v3, v4)

    visited.remove(pos)

    return v


min_dist = search((0,0), (l, l), 0)
print(min_dist)





print(f"----- {time.time() - start_time} -----")