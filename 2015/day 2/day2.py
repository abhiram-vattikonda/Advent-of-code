
with open("inp2.txt") as f:
    lines = f.read().splitlines()


# Part 1
feet = 0
rib_feet = 0
for line in lines:
    l, w, h = list(map(int, line.split('x')))
    feet += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

    len_rib = min(2*(l+w), 2*(l+h), 2*(h+w))
    rib_feet += len_rib + l*w*h



print(feet)
print(rib_feet)