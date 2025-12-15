import time

start_time = time.time()

with open("test.txt") as f:
    lines = f.read().splitlines()

lines = [line.split() for line in lines]

def conv_inputs(lines: list[list[str]]):
    outputs = [ ["1" if sin=='#' else '0' for sin in line[0][1:-1]] for line in lines]
    jolts = [[int(i) for i in line[-1][1:-1] if i!=','] for line in lines]
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

def is_safe(tup, curr_jolt, rec_jolt):
    curr = 0
    for i, val in enumerate(tup):
        if curr_jolt[val]+1 > rec_jolt:
            return False
    
    return True

    
def check_jolts(rec_jolt, curr_jolt):
    for i, val in enumerate(rec_jolt):
        if val != curr_jolt:
            return False
    
    return True


def clac_jolts(line :list[tuple], rec_jolt :list[int], curr_jolt :list[int], result):

    if check_jolts(rec_jolt, curr_jolt):
        result = []
        return
    
    for tup in line:
        if is_safe(tup, curr_jolt, rec_jolt):
            for i in tup:
                curr_jolt[i] += 1
                

        
    


lines, jolts, outputs = conv_inputs(lines)

# PART 1
lines_bin, outputs_bin = conv_bin(lines, jolts, outputs)
no_clicks = 0
for i, output in enumerate(outputs_bin):
    no_clicks += subset_xor(lines_bin[i], output)
print(f"Part 1: {no_clicks}")

# PART 2
total_clicks = 0
for i, jolt in enumerate(jolts):
    result = []
    clac_jolts(lines[i], jolt, [0]*len(jolt), result)
    print(result)
print(total_clicks)

print(f"----- {time.time() - start_time} -----")
