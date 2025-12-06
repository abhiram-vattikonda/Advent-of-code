import time

start_time = time.time()

with open("inp6.txt") as f:
    lines = f.read().splitlines()

# Part 1
# ops = lines[-1].split()
# total_sum = 0
# vals = []
# for i, line in enumerate(lines[:-1]):
#     vals.append(list(map(int, line.split())))

# for i, op in enumerate(ops):
#     if op == '+':
#         sum = 0
#         for l in vals:
#            sum += l[i] 
#     if op == '*':
#         sum = 1
#         for l in vals:
#             sum *= l[i]
    
#     total_sum += sum
# print("Part 1: ", total_sum)


# Part 2
def mul(nums):
    sum = 1
    for num in nums:
        sum *= num

    return sum


def get_nums(i :int, k :int):
    rows = len(lines[:-1])
    hor_nums = []
    for l in range(rows):
        hor_nums.append(lines[l][i:k])

    ver_nums = []
    for l in range(len(hor_nums[0][:-1])):
        num = ""
        for row in range(len(hor_nums)):
            num += hor_nums[row][l]
        ver_nums.append(int(num))

    return ver_nums

total_sum = 0
i = 0
while i < len(lines[-1]):
    char = lines[-1][i]
    k = i + 1
    try:
        while lines[-1][k] == ' ':
            k += 1
    except IndexError:
        break

    nums = get_nums(i, k)
    print(nums)


    if char == '+':
        # print(sum(nums))
        total_sum += sum(nums)
    elif char == '*':
        # print(mul(nums))
        total_sum += mul(nums)
    else:
        break
    
    i = k

print(f"Part 2: {total_sum}")

print(f"----- {time.time() - start_time} -----")