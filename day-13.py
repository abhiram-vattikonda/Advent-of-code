# add two new lines for the puzzle brfore doing

def addtuple(a:tuple, b:tuple):
    return tuple(map(lambda i, j: i + j, a, b))

def parsedata(data : list[str]):
    a = []
    b = []
    res = []
    for i,d in enumerate(data):
        if i % 4 == 0:
            a.append([int(x.strip().split('+')[1]) for x in d.split(':')[1].split(',')])
        elif i % 4 == 1:
            b.append([int(x.strip().split('+')[1]) for x in d.split(':')[1].split(',')])
        elif i % 4 == 2:
            # the '+10000000000000' should be there for part2, but should be removed for part 1
            res.append([int(x.strip().split('=')[1])+10000000000000 for x in d.split(':')[1].split(',')])
        else:
            pass

    return a, b, res

def aoc13():
    data = []
    with open('puzzle13.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    mechines = int(len(data) / 4)
    print(mechines)

    a, b, end = parsedata(data)
    sum = 0
    for i in range(mechines):
        n = -(b[i][0]*end[i][1] - b[i][1]*end[i][0]) / (a[i][0]*b[i][1] - a[i][1]*b[i][0])
        m = -(end[i][0]*a[i][1] - end[i][1]*a[i][0]) / (a[i][0]*b[i][1] - a[i][1]*b[i][0])
        
        if n - round(n) == 0:
            n = int(n)
        if m - round(m) == 0:
            m = int(m)
        
        if type(n) == int and type(m) == int:
            sum += 3*n + m
      
    print(sum)

aoc13()
