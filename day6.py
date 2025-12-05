import time
from collections import Counter

start_time = time.time()
    
def get_start_end_mode(line):
    mode = -1 # 1 - turn on, 2 - toggle, 3 - turn off
    words = line.split(' ')
    if 'on' in words: 
        mode = 1
        st, end = words[2], words[-1]
    elif 'off' in words: 
        mode = 3
        st, end = words[2], words[-1]
    else: 
        mode = 2
        st, end = words[1], words[-1]

    return st, end, mode




with open("inp6.txt") as f:
    lines = f.read().splitlines()

on = {}

mode = -1 # 1 - turn on, 2 - toggle, 3 - turn off


for line in lines:
    start, end, mode = get_start_end_mode(line)   
    stx, sty = tuple(map(int, start.split(',')))
    endx, endy = tuple(map(int, end.split(',')))

    for y in range(sty, endy +1):
        for x in range(stx, endx +1):
            loc = (x, y)
            if mode == 1: on.update({loc : 1})
            elif mode == 3: on.update({loc : 0})
            elif mode == 2: on.update({loc : 1 - (on.get(loc) if on.get(loc) is not None else 0)})


print(Counter(on.values()))
    

    

print(f"----- {time.time() - start_time} -----")