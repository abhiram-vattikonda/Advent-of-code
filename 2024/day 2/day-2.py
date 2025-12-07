def aoc2():
    data : list[list] = []

    with open("puzzle2.txt", 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    def check(x, increasing=True, change=False, correct=True):
        problem = []
        pindex = -1
        n = len(x)
        for i in range(n - 1):
            y = x[i]
            z = x[i + 1]

            # detect direction changes (kept your original idea)
            if y > z and i == 0:
                increasing = False

            if y < z and increasing == False:
                change = True
                problem.append(z)
                pindex = i + 1

            if y > z and increasing == True:
                change = True
                problem.append(z)
                pindex = i + 1

            diff = abs(y - z)
            if diff < 1 or diff > 3:
                correct = False
                problem.append(z)
                pindex = i + 1

        return pindex, problem, increasing, change, correct

    points = 0
    p2 = 0
    tp = 0
    for x in data:
        correct = True
        increasing = True
        change = False

        pindex, problem, increasing, change, correct = check(x, increasing, change, correct)

        if correct and not change:
            points += 1
            p2 += 1
            tp += 1
            continue

        # If there is exactly one reported problematic element, try removing it
        if len(problem) == 1 and pindex != -1:
            tp += 1
            # copy BEFORE popping so the original x stays unchanged
            temp = x.copy()
            # try removing the reported element
            temp.pop(pindex)
            npindex, nproblem, _, _, ncorrect = check(temp, True, False, True)
            if ncorrect and not nproblem:
                p2 += 1
                continue

            # try removing the previous element (only if pindex-1 in range)
            if pindex - 1 >= 0:
                temp2 = x.copy()
                temp2.pop(pindex - 1)
                npindex, nproblem, _, _, ncorrect = check(temp2, True, False, True)
                if ncorrect and not nproblem:
                    p2 += 1
                    continue

        # otherwise do nothing (not valid by your rule)

    print(points)
    print(p2)
    print(tp)

aoc2()
