import time
start_time =  time.time()

with open("test.txt") as f:
    lines = f.read()

class shape:
    points = []
    size = (0,0)
    center = (0, 1)
    
    def __init__(self, shape :list[str]):
        self.points = []
        self.size = (len(shape), len(shape[0]))
        self.center = (len(shape)//2, len(shape[0])//2)
        for i, line in enumerate(shape):
            for j, syn in enumerate(line):
                if syn == '#':
                    self.points.append((j, i))
        
        list(set(self.points))

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

for shp in shapes:
    shp.rotate_left()
    shp.print_shape()
    print()

print(f"----- {time.time() - start_time} -----")