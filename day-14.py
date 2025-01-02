import math

def parsedata(data : list[str]):
    p = []
    v = []
    for i, x in enumerate(data):
        a,b = x.split()
        p.append([int(x) for x in a.split('=')[1].split(',')])
        v.append([int(x) for x in b.split('=')[1].split(',')])
    return p, v


def clustered(seconds, pos,width, height):

    count = 0

    for i in range(height // 3):
        for j in range(width // 3):
            t = [width//3 + j, height//3 + i]
            if t in pos:
                count += 1


    return count >= 75



def p2(width, height, p ,v):
    count = len(p)
    pos = []
    for seconds in range(7050,7200):
        print(seconds)
        for i, t in enumerate(p):
            x2 = (p[i][0] + v[i][0] * seconds) % width
            y2 = (p[i][1] + v[i][1] * seconds) % height
            x = x2 if x2>=0 else x2 + width
            y = y2 if y2>=0 else y2 + height
            pos.append([x,y])

        with open('text.txt', 'a') as file:
            for i in range(103):
                for j in range(101):
                    if [j, i] in pos:
                        file.write("#")
                    else:
                        file.write(".")

                file.write("\n")

            file.write(f"------| {seconds} |-------\n\n")
        pos.clear()


def aoc14():
    data = []
    with open('puzzle14.txt', 'r') as file:
        for line in file:
            data.append(line.strip())


    width = 101
    height = 103
    print(width//2, height)
    p, v = parsedata(data)
    seconds = 100

    quads = [0,0,0,0]
    for i, t in enumerate(p):
        x2 = (p[i][0] + v[i][0] * seconds) % width
        y2 = (p[i][1] + v[i][1] * seconds) % height
        x = x2 if x2>=0 else x2 + width
        y = y2 if y2>=0 else y2 + height

        if x == width //2 or y == height //2:
            continue
        qx = x // (width//2)
        qy = y // (height//2)

        quad = qx + 1 if qx < 2 else qx
        quad += 2 if qy > 0 else 0  
        quads[quad-1] += 1
        #print(f"{x, y} and {quad}")

    print(quads)
    print(math.prod(quads))
    print(len(p))


    p2(width, height, p, v)

aoc14()
