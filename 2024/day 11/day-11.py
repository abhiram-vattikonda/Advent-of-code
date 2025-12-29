from functools import cache

@cache
def remake(data, steps) -> list:

    if steps == 0:
        return 1
    
    if data == 0:
        return remake(1, steps -1)
    
    lenght = len(str(data))
    if lenght % 2 == 0:
        return remake(int(str(data)[:lenght//2]), steps - 1) + remake(int(str(data)[lenght//2:]), steps - 1)
    
    return remake(data*2024, steps - 1)

def aoc10():
    data = []
    with open('test.txt', 'r') as file:
        data = [int(x) for x in file.read().split()]

    sum = 0
    count = 75
    for d in data:
        sum += remake(d, count)
        
        

    #print (data)
    print (sum)



aoc10()