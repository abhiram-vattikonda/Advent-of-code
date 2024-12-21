

def aoc1():
    A = []
    B = []
    with open("puzzle1.txt", 'r') as file:
        for line in file:
            a, b = line.split()
            A.append(int(a))
            B.append(int(b))

    A = sorted(A)
    B = sorted(B)


    sum = 0
    sim = dict({})

    for i, x in enumerate(A):
        #print(f"{x} and {B[i]}")
        sum += abs(x - B[i])
        sim[x] = 0

    for x in B:
        if x in sim:
            sim[x] += 1
        

    newsum = 0
    for x in A:
        #print(f"{x} and {sim[x]}")
        newsum += x * sim[x]
    
    print(sum)
    print(newsum)


aoc1()