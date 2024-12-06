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
iscorrect = True
for i in range(0, len(updates)):
    iscorrect = True
    for j in range(1, len(updates[i])):
        for k in range(0, j):
            try:
                if updates[i][k] in rules[updates[i][j]]:
                    iscorrect = False
                    break
            except KeyError:
                continue
        if iscorrect is False:
            break
    if iscorrect is True:
        correct.append(updates[i])
    
sum = 0
for a in range(0, len(correct)):
    sum += int(correct[a][int(len(correct[a])/2)])
print(sum)
