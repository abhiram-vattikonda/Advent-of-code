

with open("inp3.txt") as f:
    line = f.read()

# line = '^>v<'
directions = {
    '<' : (-1, 0),
    '>' : (1, 0),
    '^' : (0, -1),
    'v' : (0, 1)
}


# Part 1
# curr_pos = (0, 0)
# gifts = {(0, 0) : 1}
# for sym in line:
#     move = directions[sym]
#     curr_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
#     if gifts.get(curr_pos):
#         gifts[curr_pos] += 1
#     else:
#         gifts.update({curr_pos : 1})

# k = sorted(gifts.values(), reverse=True)
# print(k)

# count = 0
# for i in k:
#     if i >= 1:
#         count += 1
#     else:
#         break
        
# print(count)
# print(gifts)


curr_pos = [(0, 0), (0, 0)]
gifts = [{(0, 0) : 1}, {(0, 0) : 1}]
turn = 0

for sym in line:
    move = directions[sym]
    curr_pos[turn] = (curr_pos[turn][0] + move[0], curr_pos[turn][1] + move[1])
    if gifts[turn].get(curr_pos[turn]):
        gifts[turn][curr_pos[turn]] += 1
    else:
        gifts[turn].update({curr_pos[turn] : 1})

    turn = 1 - turn

k = gifts[0] | gifts[1]

count = 0
for i in k:
    if k[i] >= 1:
        count += 1
        
print(count)
#


