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
end = (l, l)

def search(p0, p1, steps):
    
    # vis = visited.copy()
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    if (p0, p1) == end:
        # print(f"Steps: {steps}")
        return steps

    if (p0, p1) in blocks:
        return float("infinity")
    
    if 0 > p0 or p0 > l or 0 > p1 or p1 > l:
        return float("infinity")
    
    if (p0, p1) in visited:
        return float("infinity")

    visited.append((p0, p1))

    a, b = addtuple((p0, p1), direction[0])
    v1 = search(a, b, steps+1)

    a, b = addtuple((p0, p1), direction[1])
    v2 = search(a, b, steps+1)

    a, b = addtuple((p0, p1), direction[2])
    v3 = search(a, b, steps+1)

    a, b = addtuple((p0, p1), direction[3])
    v4 = search(a, b, steps+1)

    v = min(v1, v2, v3, v4)

    visited.remove((p0, p1))

    return v


min_dist = search(0,0, 0)
print(min_dist)





print(f"----- {time.time() - start_time} -----")