map = []
while True:
    raw = input()
    if raw == "":
        break
    map.append(list(raw))

tempx = 0
tempy = 0
for i in range(0, len(map)):
    try:
        tempx = map[i].index("^")
        tempy = i
    except ValueError:
        continue

char = '^'
blocks = 0
secmap = []

for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        x = tempx
        y = tempy
        char = '^'
        for a in map:
            secmap.append(a.copy())

        secmap[i][j] = '#'
        count = 0
        loop = 0

        '''print()
        print()
        for a in secmap:
            print("".join(a))'''

        
        
        while loop < 500000:
            try:
                loop += 1
                secmap[y][x] = 'X'

                if char == '^' and secmap[y-1][x] == "#":
                    char = '>'
                elif char == 'v' and secmap[y+1][x] == "#":
                    char = '<'
                elif char == '>' and secmap[y][x+1] == "#":
                    char = 'v'
                elif char == '<' and secmap[y][x-1] == "#":
                    char = '^'
                
                if char == '^':
                    y -= 1
                elif char == 'v':
                    y += 1
                elif char == '>':
                    x += 1
                elif char == '<':
                    x -= 1

                if secmap[y][x] =='.':
                    count += 1
                secmap[y][x] = char

            except IndexError:
                break
     
        #print(count + 1)
        if loop >= 500000:
            blocks += 1

        secmap.clear()

print(blocks)