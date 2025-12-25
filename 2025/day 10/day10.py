import time

start_time = time.time()

with open("inp10.txt") as f:
    lines = f.read().splitlines()

lines = [line.split() for line in lines]

def conv_inputs(lines: list[list[str]]):
    outputs = [ ["1" if sin=='#' else '0' for sin in line[0][1:-1]] for line in lines]
    jolts = [list(map(int, line[-1][1:-1].split(','))) for line in lines]
    lines = [[tuple([int(sin) for sin in i[1:-1] if sin!=',']) for i in line[1:-1] ] for line in lines]

    # print(outputs)
    # print(jolts)
    # print(lines)
    return lines, jolts, outputs

def tup_to_bin(tup :tuple[int], len :int):
    b = ['0']*len
    for i in tup:
        b[i] = '1'
    
    return ''.join(b)



def conv_bin(lines :list[list[tuple]], jolts :list[list[int]], outputs :list[list[int]]):

    lines_bin = [[int(tup_to_bin(t, len(outputs[i])),2) for t in line] for i, line in enumerate(lines)]
    outputs_bin = [int(''.join(o), 2) for o in outputs]



    # print(outputs_bin)
    # print(lines_bin)
    return lines_bin, outputs_bin


def subset_xor(nums, target):
    if target == 0:
        return 0
    dp = {0 : 0}  # XOR of empty subset is 0

    for i, num in enumerate(nums):
        new_vals = {}
        for x in dp:
            if dp.get(x^num):
                new_vals.update({x ^ num : min(dp[x]+1, dp[x^num])})
            else:
                new_vals.update({x ^ num : dp[x]+1})
        
        for d in new_vals:
            if d in dp:
                dp.update({d : min(new_vals[d], dp[d])})
            else:
                dp.update({d : new_vals[d]})


    if target in dp:
        return dp[target]
    else:
        print("qwerty")
        return 1

 
def calc_presses_jolts(buttons :list, goal :list[int], curr :list[int]):
    print(curr)
    if goal == curr:
        return 1
    
    if any( [k if curr[i] > k else 0 for i, k in enumerate(goal) ] ):
        return 0
    
    min_presses = float('inf')
    for button in buttons:
        for n in button:
            curr[n] += 1
        
        val = calc_presses_jolts(buttons, goal, curr)
        if val:
            min_presses = min(min_presses, val)

        for n in button:
            curr[n] -= 1
        
        print("---")

    
    return 1 + min_presses
    
    


lines, jolts, outputs = conv_inputs(lines)

# PART 1
lines_bin, outputs_bin = conv_bin(lines, jolts, outputs)
no_clicks = 0
for i, output in enumerate(outputs_bin):
    no_clicks += subset_xor(lines_bin[i], output)
print(f"Part 1: {no_clicks}")

# PART 2
# total_clicks = 0
# for i, line in enumerate(lines):
#     p = calc_presses_jolts(line, jolts[i], [0]*len(jolts[i]))
#     print(p - 1)
#     total_clicks += p
# print("Part 2: ", total_clicks)

import numpy as np
from z3 import Int, Optimize, Sum

total = 0
for i, line in enumerate(lines):
    mat = np.array([[1 if j in button else 0 for j in range(len(outputs[i]))] for button in line])

    mat = mat.transpose()
    # print(mat)
    b = jolts[i]

    m = len(mat)
    n = len(mat[0])

    x = [Int(f"x{i}") for i in range(n)]

    s = Optimize()

    for xi in x:
        s.add(xi >= 0)

    for i in range(m):
        s.add(Sum(mat[i][j] * x[j] for j in range(n)) == b[i]) 

    s.minimize(Sum(x))
    
    if s.check():
        model = s.model() 
        total += sum(model[xi].py_value() for xi in x)

print("Part 2:", total)
# 15811 too low with 10

print(f"----- {time.time() - start_time} -----")
