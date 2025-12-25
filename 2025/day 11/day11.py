import time
from functools import cache
start_time = time.time()

with open("inp11.txt") as f:
    lines = f.read().splitlines()

connections = {node.split()[0][:-1] : node.split()[1:] for node in lines}
# print(connections)

# Part 1, easy input, without loops, this fails if there are loops
@cache
def get_paths(start :str, end :str):
    if start == end:
        return 1
    
    tsum = 0
    for i in connections[start]:
        p = get_paths(i, end)
        tsum += p
    
    return tsum

start = 'svr'
end = 'out'
tpaths = get_paths(start, end)
print("Part 1: ", tpaths)

# Part 2
@cache
def get_paths_v2(start :str, end :str, fft :bool = False, dac :bool = False):
    if start == end:
        if fft and dac:
            return 1, fft, dac
        else:
            return 0, fft, dac
    
    if start == 'fft':
        fft = True
    if start == 'dac':
        dac = True

    tsum = 0
    for i in connections[start]:
        p, fft, dac = get_paths_v2(i, end, fft, dac)
        
        tsum += p

    if start == 'fft':
        fft = False
    if start == 'dac':
        dac = False

    return tsum, fft, dac


start = 'svr'
end = 'out'

paths = get_paths_v2(start, end)
print("Part 2: ", paths[0])



# 23036892780241 is too low

print(f"----- {time.time() - start_time} -----")