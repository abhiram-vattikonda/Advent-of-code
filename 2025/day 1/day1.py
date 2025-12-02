import re

with open("inp1.txt") as f:
    rotations = f.read().split("\n")

dial  = 50
zeros = 0

# for rotation in rotations:
#     if 'L' in rotation:
#         dial = (dial - int(rotation[1:])) % 100
#     elif 'R' in rotation:
#         dial = (dial + int(rotation[1:])) % 100
#     else:
#         print(f"no L or R in {rotation}")
#     if dial == 0:
#         zeros += 1


for rotation in rotations:
    initialdial = dial
    if 'L' in rotation:
        rc = int(rotation[1:])
        dialchange = rc % 100
        spins = rc // 100
        dial -= dialchange

    elif 'R' in rotation:
        rc = int(rotation[1:])
        dialchange = rc % 100
        spins = rc // 100
        dial += dialchange


    else:
        print(f"no L or R in {rotation}")

    zeros += spins
    if (dial >= 100 or dial <= 0) and initialdial != 0:
        zeros += 1
        #print("+1  ", end="")

    #print(f"{rotation}  {initialdial} -->  {dial}")
    dial %= 100

    # dial %= 100

#2621 is low




print(zeros)
