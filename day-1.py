

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

    for i, x in enumerate(A):
        #print(f"{x} and {B[i]}")
        sum += abs(x - B[i])
    
    print(sum)


aoc1()