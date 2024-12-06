map = []
while True:
    raw = input()
    if raw == "":
        break
    map.append(raw)

x = 0
y = 0
for i in range(0, len(map)):
    x = map[i].find("^")
    if x != -1:
        y = i

print(map[y])