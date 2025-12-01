import re

with open("test.txt") as f:
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
print(rotations)
for rotation in rotations:
    if 'L' in rotation:
        dial = (dial - int(rotation[1:]))

    elif 'R' in rotation:
        dial = (dial + int(rotation[1:]))

    else:
        print(f"no L or R in {rotation}")

    print(rotation, "  ", dial, end = " ")
    if dial >= 100 or dial <= 0:
        zeros += 1
        dial %= 100
        print(dial)
        print(" +1 = ", zeros)
    # dial %= 100
    # print(dial)




print(zeros)
