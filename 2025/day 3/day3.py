import time
from collections import Counter

start_time = time.time()

with open("inp3.txt") as f:
    lines = f.read().splitlines()

val = 0

# Part 1
# for line in lines:
#     highest = -1
#     first, second = 0, 0
#     for i in range(len(line)):
#         for j in range(i + 1, len(line)): 
#             num = int(line[i])*10 + int(line[j])
#             if num > highest: 
#                 highest = num
#                 first, second = i, j
    
#     val += highest
#     print(f"Line: {line} | Highest: {highest}")

            
# Part 2
for line in lines:
    nums = list(map(int, list(line)))
    
    print(nums)
    print(Counter(nums))
    start_index = -1
    c = 12
    l = reversed(range(c))
    n = ""
    for k in l:
        haha = nums[start_index+1:len(nums) - k]
        max_num = max(haha)
        n += str(max_num)

        for i in range(start_index+1, len(nums)):
            if nums[i] == max_num:
                start_index = i
                break
    
    print(n)    
    print()

    val += int(n)

        
    



print()
print(val)



print(f"----- {time.time() - start_time} -----")