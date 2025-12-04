

with open("inp5.txt") as f:
    lines = f.read().splitlines()



# Part 1
# count = 0
# need_cont = False
# for line in lines:
#     for com in ['ab', 'cd', 'pq', 'xy']:
#         if com in line:
#             need_cont = True
#             break
    
#     if need_cont:
#         need_cont = False
#         continue

#     vowel_count = 0
#     for i in ['a', 'e', 'i', 'o', 'u']:
#         for j in line:
#             if i == j:
#                 vowel_count += 1
    
#     if vowel_count < 3:
#         continue

#     has_double = False
#     for i in range(len(line)-1):
#         if line[i] == line[i+1]:
#             has_double = True
#             break
    
#     if not has_double:
#         continue

#     print(line)
#     count += 1

    

# print(count)       



# Part 2
count = 0
for line in lines:
    has_pair = False
    for i in range(len(line)-1):
        pair = line[i:i+2]
        for j in range(i+2, len(line)-1):
            if pair == line[j:j+2]:
                has_pair = True
                break
        if has_pair:
            break

    if not has_pair:
        continue

    has_repeat = False
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            has_repeat = True
            break
    
    if not has_repeat:
        continue

    print(line)
    count += 1

print(count)