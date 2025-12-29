def aoc2():
    data : list[list] = []

    with open("puzzle2.txt", 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    def check(x, increasing=True, correct=True):
        n = len(x)
        for i in range(n - 1):
            y = x[i]
            z = x[i + 1]

            if y > z and i == 0:
                increasing = False

            if y < z and not increasing:
                return False

            if y > z and increasing:
                return False

            diff = abs(y - z)
            if diff < 1 or diff > 3:
                return False
        
        return True

    p1 = 0
    p2 = 0
    for x in data:
        if check(x):
            p1 += 1
            p2 += 1

        else:

            for i, y in enumerate(x):
                temp = x.copy()
                temp.pop(i)
                if check(temp):
                    p2 += 1
                    break


    print(p1)
    print(p2)


aoc2()
