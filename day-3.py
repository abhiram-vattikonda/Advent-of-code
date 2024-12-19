import re

def aoc3():
    data = []
    with open("puzzle3.txt", 'r') as file:
        for line in file:
            data.append(line)

    sum = 0
    do = True

    reg = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
    for x in data:
        li = re.findall(reg, x)
        #print(li)
        for y in li:
            if do == False and y[1] == 'do()':
                do =True
                continue
            
            if do == True and y[2] == "don't()":
                do = False
                continue

            if do == True and y[1] == '' and y[2] == '':
                a,b = re.search(r"\d{1,3},\d{1,3}", y[0])[0].split(',')
                sum += int(a) * int(b)

            #print(sum)

    print(sum)
aoc3()