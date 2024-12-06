map = []
while True:
    raw = input()
    if raw == "":
        break
    map.append(list(raw))

x = 0
y = 0
for i in range(0, len(map)):
    try:
        x = map[i].index("^")
        y = i
    except ValueError:
        continue

char = '^'
count = 0
while True:
    try:
        map[y][x] = 'X'

        if char == '^' and map[y-1][x] == "#":
            char = '>'
        elif char == 'v' and map[y+1][x] == "#":
            char = '<'
        elif char == '>' and map[y][x+1] == "#":
            char = 'v'
        elif char == '<' and map[y][x-1] == "#":
            char = '^'
        
        if char == '^':
            y -= 1
        elif char == 'v':
            y += 1
        elif char == '>':
            x += 1
        elif char == '<':
            x -= 1

        if map[y][x] =='.':
            count += 1
            map[y][x] = char

    except IndexError:
        break


print(count + 1)