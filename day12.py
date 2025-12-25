import time
start_time =  time.time()

with open("inp12.txt") as f:
    lines = f.read()

class shape:
    points = []
    size = (0,0)
    center = (0, 1)
    area = 0
    
    def __init__(self, shape :list[str]):
        self.points = []
        self.size = (len(shape), len(shape[0]))
        self.center = (len(shape)//2, len(shape[0])//2)
        area = 0
        for i, line in enumerate(shape):
            for j, syn in enumerate(line):
                if syn == '#':
                    self.points.append((j, i))
                    area += 1
        
        list(set(self.points))
        self.area = area

    def rotate_right(self):
        cx, cy = self.center
        self.points = [
            (-(y - cy) + cx, (x - cx) + cy)
            for x, y in self.points
        ]

    def rotate_left(self):
        cx, cy = self.center
        self.points = [
            ((y - cy) + cx, -(x - cx) + cy)
            for x, y in self.points
        ]


    
        
    def print_shape(self):
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if (j, i) in self.points:
                    print("#", end='')
                else:
                    print('.', end='')
            print()


lines = lines.split('\n\n')

shapes_str = [line.split('\n') for line in lines[:-1]]
spaces = lines[-1].split('\n')

shapes = []
for shape_str in shapes_str:
    shapes.append(shape(shape_str[1:]))

spaces = [space.split(' ') for space in spaces]
spaces = [[tuple(map(int, (space[0][:-1]).split('x'))), list(map(int, space[1:]))] for space in spaces]

# Part 1 but using a trick, this only works for this input not a general solution
# we should solve it using pack
# fits_count = 0
# for space, gifts in spaces:
#     area_present = space[0] * space[1]
#     area_gifts = 0
#     for i, k in enumerate(gifts):
#         area_gifts += k * shapes[i].area

#     if area_present > area_gifts:
#         fits_count += 1





print("Part 1: ", fits_count)

print(f"----- {time.time() - start_time} -----")