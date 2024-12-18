from ordered_set import OrderedSet

def locationcont(antenne, height, width) -> int:
    spots = OrderedSet({})
    for value in antenne.keys():
        for i in range(len(antenne[value])):
            for j in range(i + 1, len(antenne[value])):
                p = antenne[value][i]
                q = antenne[value][j]
                spots.add(p)
                spots.add(q)

                # find the 2 positions
                diff = (p[0] - q[0], p[1] - q[1])
                a = (p[0] + diff[0], p[1] + diff[1])
                b = (q[0] - diff[0], q[1] - diff[1])

                # check if in bounds
                while 0 <= a[0] < width and 0 <= a[1] < width:
                    spots.add(a)
                    a = (a[0] + diff[0], a[1] + diff[1])
                while 0 <= b[0] < width and 0 <= b[1] < width:
                    spots.add(b)
                    b = (b[0] - diff[0], b[1] - diff[1])
            
    #print(spots)
    return len(spots)

def locations(antenne, height, width) -> int:
    spots = OrderedSet({})

    for value in antenne.keys():
        for i in range(len(antenne[value])):
            for j in range(i + 1, len(antenne[value])):
                p = antenne[value][i]
                q = antenne[value][j]

                # find the 2 positions
                diff = (p[0] - q[0], p[1] - q[1])
                a = (p[0] + diff[0], p[1] + diff[1])
                b = (q[0] - diff[0], q[1] - diff[1])

                # check if in bounds
                if 0 <= a[0] < width and 0 <= a[1] < width:
                    spots.add(a)
                if 0 <= b[0] < width and 0 <= b[1] < width:
                    spots.add(b)
    #print(spots)
    return len(spots)


def aoc8():
    #take in put
    data = []
    while True:
        x = input()
        if x == '':
            break
        data.append(x)
    
    height = len(data)
    width = len(data[0])
    antenne = {}

    #print(antenne)
    print()
    for row in range(len(data)):
        for column in range(len(data[0])):
            item = data[row][column]
            if item != '.':
                if item in antenne:
                    antenne[item].append((column, row))
                else:
                    antenne.update({item : [(column, row)]})

    #count = locations(antenne, height, width)
    total = locationcont(antenne, height, width)
    #print(count)
    print(total)

    


    #print(antenne)
    pass


aoc8()