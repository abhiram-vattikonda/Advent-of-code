
with open("inp1.txt") as f:
    line = f.read()

# Part 1, Part 2
val = 0
pos = 0
for bracket in line:
    pos += 1
    if bracket == '(':
        val += 1
    elif bracket == ')':
        val -= 1
    
    if val == -1:
        print(f"Entered Basement at {pos}")

print(val)