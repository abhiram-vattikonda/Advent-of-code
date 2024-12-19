

def aoc2():
    data = []

    with open("puzzle2.txt", 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    points = 0
    for x in data:
        correct = True
        increasing = True
        change = False
        for i, y in enumerate(x):
            if i == len(x) - 1:
                break
        
            if y > x[i+1] and i == 0:
                increasing = False

            if y < x[i+1] and increasing == False:
                change = True
            if y > x[i+1] and increasing == True:
                change = True

            diff = abs(y - x[i+1])
            if 1 > diff or diff > 3:
                correct = False
                break
        
        if correct and not change:
            points += 1

    #print(data)
    print(points)


aoc2()