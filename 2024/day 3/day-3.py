import time, re

start_time = time.time()

with open("puzzle3.txt") as f:
    lines = f.read().splitlines()
# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

patter = r"mul\(([0-9]+,[0-9]+)\)|(do\(\))|(don't\(\))"

sum = 0
for line in lines:
    muls = re.findall(patter, line)
    # print(muls)
    muls = [i[k] for i in muls for k in range(3) if i[k] != '']
    
    print(muls)

    mul = []
    add = True
    for m in muls:
        if (m != "don't()" and m != "do()") and add:
            mul.append(m)

        else:
            if m == "don't()":
                add = False
            elif m == "do()":
                add = True
        
    mul = [tuple(map(int, i.split(','))) for i in mul]
    # print(mul)
    for a in mul:
        print(a)
        sum += a[0] * a[1]

print(sum)
# 102360389 is too high

print(f"----- {time.time() - start_time} -----")