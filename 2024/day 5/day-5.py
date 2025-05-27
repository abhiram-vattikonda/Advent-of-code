from functools import cmp_to_key

def check(row):
    iscorrect = True
    for j in range(1, len(row)):
        for k in range(0, j):
            try:
                if row[k] in rules[row[j]]:
                    iscorrect = False
                    break
            except KeyError:
                continue
        if iscorrect is False:
            if not p2:
                incorrect.append(list(row))
            break
    if iscorrect is True:
        correct.append(list(row))
        return True
    
    return False

def compare(y, x):
    if x in rules:
        return -1 if y in rules[x] else 1
    
    return 0


p2 = False
rules = {str : list()}
while True:
    rawrule = input()
    if rawrule == "":
        break
    x = rawrule.partition("|")
    try:
        rules[x[0]].append(x[2])
    except KeyError:
        rules.update({x[0] : []})
        rules[x[0]].append(x[2])

updates = []
while True:
    rawupdate = input()
    if rawupdate == "":
        break
    y = rawupdate.split(",")
    updates.append(y)

correct = []
incorrect = []
iscorrect = True
for i in range(0, len(updates)):
    check(updates[i])
    
    
sum = 0
for a in range(0, len(correct)):
    sum += int(correct[a][int(len(correct[a])/2)])
print(f"part1: {sum}")

for i in incorrect:
    i.sort(key=cmp_to_key(compare))


sum = 0
for a in range(0, len(incorrect)):
    sum += int(incorrect[a][int(len(incorrect[a])/2)])
print(f"part2: {sum}")

"""p2 = True
print(*incorrect)
correct.clear()
for i in range(len(incorrect)):
    for a in range(len(incorrect[i])):
        t = incorrect[i].pop(a)
        for b in range(len(incorrect[i]) + 1):
            incorrect[i].insert(b, t)
            gotit = check(incorrect[i])
            incorrect[i].pop(b)
            if gotit:
                break
        incorrect[i].insert(a, t)
        if gotit:
            break
    print(*correct)"""

           



