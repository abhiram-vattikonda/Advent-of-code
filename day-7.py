def canform(result, nums):
    
    
    
    pass

def aoc7():
    #take in put
    data = []
    while True:
        x = input()
        if x == '':
            break
        data.append(x)
    
    #parse input and find solution
    total = 0
    for i in data:
        result, nums = i.split(": ")
        result = int(result)
        nums = [int(x) for x in nums.split()]
        if canform(result, nums):
            total += 1
        
    print(total)

aoc7()