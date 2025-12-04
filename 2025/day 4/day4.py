import time

start_time = time.time()

def Check_adj(x :int, y :int):
    count = 0
    for direction in directions:
        addx, addy = direction
        if 0 <= y + addy < Y and 0 <= x + addx < X and lines[y + addy][x + addx] == '@':
            count += 1
        
        if count >= 4:
            return False
    
    return True

    

directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]

with open("inp4.txt") as f:
    lines = f.read().splitlines()

papers = 0
Y = len(lines)
X = len(lines[0])

# Part 1
# for line in range(Y):
#     for x in range(X):
#         if lines[line][x] != '@':
#             continue
    
#         if Check_adj(x, line):
#             papers += 1

moved = True

while moved:
    count_per_epoch = 0
    for line in range(Y):
        for x in range(X):
            if lines[line][x] != '@':
                continue
    
            if Check_adj(x, line):
                lines[line] = f"{lines[line][:x]}.{lines[line][x+1:]}"
                count_per_epoch += 1
                papers += 1
    
    if count_per_epoch == 0:
        break
    else:
        print(count_per_epoch)





print(papers)

print(f"----- {time.time() - start_time} -----")