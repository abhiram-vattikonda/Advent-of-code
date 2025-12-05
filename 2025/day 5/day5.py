import time

start_time = time.time()

with open("inp5.txt") as f:
    lines = f.read().splitlines()



# Part 1
# fresh_range = []
# count = 0
# i = 0
# for line in lines:
#     if '-' in line:
#         a, b = tuple(map(int, line.split('-')))

#         fresh_range.append((a, b))   
        
#     i += 1
#     if line == '':
#         break

# print(fresh_range)

# for line in lines[i:]:
#     for rng in fresh_range:
#         if rng[0] <= int(line) <= rng[1]:
#             print(line)
#             count += 1
#             break

# print(count)




fresh = set()
for line in lines:
    if '-' in line:
        a, b = tuple(map(int, line.split('-')))

        fresh.add((a, b))
    

    if line == '':
        break

# print(fresh)
sort_fresh = sorted(fresh, key=lambda x: x[0])
# print(sort_fresh)

end  = -1
count = 0
for rng in sort_fresh:
    print(rng)
    if rng[0] > end:
        count += rng[1] - rng[0] + 1

    elif rng[1] > end:
        count += rng[1] - end
    
    end = max(end, rng[1])


print(count)

# 422001555241321 too high
# 298140437737178 too low
# 347823962220526 too low
    
    
print(f"----- {time.time() - start_time} -----")