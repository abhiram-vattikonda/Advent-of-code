import time


start_time = time.time()

with open("puzzle18.txt", "r") as file:
    data = file.readlines()

data = [tuple(map(int, x.split(','))) for x in data]

l = 70
byte = 1024

blocks = data[:byte]

def addtuple(a :tuple[int], b :tuple[int]):
    return (a[0]+b[0], a[1]+b[1])

def search(pos, blocks, end, steps, visited :list[tuple[int]]):
    
   
min_dist = search((0,0), blocks, (l, l), 0, [])
print(min_dist)





print(f"----- {time.time() - start_time} -----")