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
from sympy import Matrix    
import sympy as sp
from itertools import product
from functools import cache


def extract_solution(solution, taus):
    x_exprs = [solution[i, 0] for i in range(solution.rows)]
    tau_syms = list(taus)
    return x_exprs, tau_syms
def constraints_satisfied(x_vals):
    return all(v >= 0 for v in x_vals)
def evaluate_x(x_exprs, tau_syms, tau_vals):
    subs = dict(zip(tau_syms, tau_vals))
    return [int(expr.subs(subs)) for expr in x_exprs]
def objective(x_vals):
    return sum(x_vals)
def generate_tau_ranges(k, max_tau):
    return [range(0, max_tau + 1) for _ in range(k)]

def minimize_sum_from_gj(A, b, max_tau=25):
    try:
        solution, taus = A.gauss_jordan_solve(b)
    except ValueError:
        return {
            "status": "no_solution"
        }

    x_exprs = [solution[i, 0] for i in range(solution.rows)]
    tau_syms = list(taus)

    # CASE 1: Unique solution (no taus)
    if len(tau_syms) == 0:
        x_vals = [int(v) for v in x_exprs]

        if not constraints_satisfied(x_vals):
            return {
                "status": "unique_solution_invalid",
                "x": x_vals
            }

        return {
            "status": "unique_solution",
            "x": x_vals,
            "sum": sum(x_vals)
        }

    # CASE 2: Infinite solutions
    best = None
    best_tau = None
    best_x = None

    tau_ranges = [range(0, max_tau + 1) for _ in tau_syms]

    for tau_vals in product(*tau_ranges):
        x_vals = evaluate_x(x_exprs, tau_syms, tau_vals)

        if not constraints_satisfied(x_vals):
            continue

        s = objective(x_vals)

        if best is None or s < best:
            best = s
            best_tau = tau_vals
            best_x = x_vals

    if best is None:
        print(solution, taus)
        print(A)
        print(b)
        return {
            "status": "infinite_solutions_no_feasible_point"
        }

    return {
        "status": "infinite_solutions",
        "taus": dict(zip(tau_syms, best_tau)),
        "x": best_x,
        "sum": best
    }



total = 0
for i in range(len(lines)):
    n = len(outputs[i])
    buttons = lines[i]
    goal = Matrix(jolts[i])
    mat = Matrix([[1 if t in b else 0 for t in range(n)] for b in buttons])
    mat = mat.transpose()
    result = minimize_sum_from_gj(mat, goal)
    print(result)
    if result['status'] != 'infinite_solutions_no_feasible_point':
        total += result['sum']
    
    

print("Part 2: ", total)

# 15811 too low with 10

print(f"----- {time.time() - start_time} -----")
