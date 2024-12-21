"""
def calcvalue(values, space, totalLetters, highestpos) -> int:
    sum = 0

    valuekeylow = 0
    valuekeyhigh = highestpos
    spacekey = 0

    for i in range(totalLetters):
        if values[valuekeylow]:
            sum += (valuekeylow * i)
            values[valuekeylow] -= 1
            print(f"{valuekeylow}", end="")
            if values[valuekeylow] == 0:
                spacekey += 1
        else:
            while valuekeyhigh >= 0 and values[valuekeyhigh] == 0:
                valuekeyhigh -= 1
            
            if valuekeyhigh < 0:
                break

            sum += (valuekeyhigh * i)
            values[valuekeyhigh] -= 1
            space[spacekey] -= 1
            print(f"{valuekeyhigh}", end='')
            if space[spacekey] == 0:
                valuekeylow += 1
    
    
    return sum


def aoc9():
    values = dict({int : int})
    space = dict({int : int})
    pos = 0
    total = 0
    name = "puzzle91.txt"
    file = open(name, 'r')
    line = file.read()
    for i, x in enumerate(line):
        if (i % 2) == 0:
            values.update({pos : int(x)})
            pos += 1
        else:
            space.update({pos : int(x)})
        total += int(x)

    
    sum = calcvalue(values, space, total, pos - 1)
    print("\n")
    print(sum)
    #print(values)
    #print(space)


aoc9()"""

name = "puzzle9.txt"

def p1():
    file = open(name, 'r')
    line = file.read()

    val = []
    pos = 0
    for i, x in enumerate(line):
        if (i % 2) == 0:
            val += [pos] * int(x)
            pos += 1
        else:
            val += [-1] * int(x)

    try:
        for a in range(len(val)):
            if val[a] == -1:
                t = val.pop()
                while t == -1:
                    t = val.pop()
                val[a] = t
    except IndexError:
        pass


    sum = 0
    for a in range(len(val)):
        sum += a * val[a]

    print(sum)

def p2():
    file = open(name, 'r')
    line = file.read()


p1()
p2()