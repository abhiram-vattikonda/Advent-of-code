import re

def aoc3():
    data = []
    with open("puzzle3.txt", 'r') as file:
        for line in file:
            data.append(line)

    sum = 0

    reg = r"mul\(\d{1,3},\d{1,3}\)"
    for x in data:
        li = re.findall(reg, x)
        for y in li:
            a,b = re.search(r"\d{1,3},\d{1,3}", y)[0].split(',')
            sum += int(a) * int(b)

    print(sum)
aoc3()