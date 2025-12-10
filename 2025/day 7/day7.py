import time
from functools import lru_cache
start_time = time.time()

with open('test.txt') as f:
    lines = f.read().splitlines()


beams = list()
for i, x in enumerate(lines[0]):
    if x == 'S':
        beams.append([i, 0])


# Part 1
# print(beams)
# splits = 0
# for i in range(1, len(lines)):
#     to_remove = []
#     print(f"line: {i}")
#     for beam in beams:
#         if lines[i][beam[0]] != '^' and beam[1] == i-1:
#             beams.append((beam[0], beam[1]+1))
#             to_remove.append(beam)
#             continue

#         elif beam[1] == i-1:
#             to_remove.append(beam)
#             beams.append((beam[0]-1, beam[1]+1))
#             beams.append((beam[0]+1, beam[1]+1))
#             splits += 1

#     for beam in to_remove:
#         beams.remove(beam)
#     beams = list(set(beams))
    
# print(splits)


# Part 2
store = {}
def move_forward(lines :list[str], beam :list, i :int):
    while i < len(lines):   
        # print(f"line: {i}")
        if lines[i][beam[0]] != '^' and beam[1] == i-1:
            beam[1] = i
        
        elif beam[1] == i-1:
            if store.get((tuple(beam), i)):
                return store.get((tuple(beam), i))
            else:
                left = move_forward(lines, [beam[0]-1, beam[1]+1], i+1)
                right = move_forward(lines, [beam[0]+1, beam[1]+1], i+1)
                store.update({(tuple(beam), i) : left+right})
                return left + right

        i += 1

    print(beam)
    return 1


beam = beams[0]
print(move_forward(lines, beam, 1))





print(f"----- {time.time() - start_time} -----")