
# this is a form of branch and bound
def canform(result, nums, i, sumtillnow, concat):
    #the two base cases
    if i == len(nums):
        return result == sumtillnow
    
    if sumtillnow > result:
        return False
    
    #Check if adding of multiplying the current sum and next will give the ans
    # if concat is true, also check for the operation with concatination
    return canform(result, nums, i+1, sumtillnow + nums[i], concat) or (concat and canform(result, nums, i+1, sumtillnow * nums[i], concat) or canform(result, nums, i+1, int(str(sumtillnow) + str(nums[i])), concat))


def aoc7():
    #take in put
    data = []
    while True:
        x = input()
        if x == '':
            break
        data.append(x)
    
    #parse input and find solution
    total1 = 0
    total2 = 0
    for i in data:
        result, nums = i.split(": ")
        result = int(result)
        nums = [int(x) for x in nums.split()]
        if canform(result, nums, 1, nums[0], False):
            total1 += result

        if canform(result, nums, 1, nums[0], True):
            total2 += result

    print(total1)
    print(total2)

aoc7()