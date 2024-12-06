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


