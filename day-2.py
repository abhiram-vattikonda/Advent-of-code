
#ya this is wrong, it will give 545, the answer is 544, i found the ans by just looking at the diff reports with
# 1 problem and i found two, the issue is we are not checking if removing the single number might further cause issues
# will leave this for now
def aoc2():
    data = []

    with open("puzzle2.txt", 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    points = 0
    p2 = 0
    for x in data:
        correct = True
        increasing = True
        change = False
        problem = []
        for i, y in enumerate(x):
            if i == len(x) - 1:
                break
        
            if y > x[i+1] and i == 0:
                increasing = False

            if y < x[i+1] and increasing == False:
                change = True
                problem += [x[i+1]]
            if y > x[i+1] and increasing == True:
                change = True
                problem += [x[i+1]]

            diff = abs(y - x[i+1])
            if 1 > diff or diff > 3:
                correct = False
                problem += [x[i+1]]
        
        if correct and not change:
            points += 1

        if len(problem) <= 1:
            p2 += 1

        if len(problem) == 1:
            print(f"{problem} and {x}")

    #print(data)
    print(points)
    print(p2)


aoc2()