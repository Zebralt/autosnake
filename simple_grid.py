
# Jocelyn Vernay, 2017

import sys

# Constants for grid content.
EMPTY = 0b0
OBSTACLE = 0b1
WATER = 0b11

def printw(strs):
    sys.stdout.write(str(strs))
    sys.stdout.flush()

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate()
        
    def get(self, x , y):
        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return None
        return self.data[x][y]
        
    def get_from_tuple(self, xy):
        x, y = xy
        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return None
        return self.data[x][y]

    def set(self, x , y, val):
        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return
        self.data[x][y] = val
    
    def set_from_tuple(self, xy, val):
        x, y = xy
        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return
        self.data[x][y] = val
    
    def generate(self):
        self.data = [[0 for i in range(self.height)] for j in range(self.width)]
    
# Simple test to see if a case is traversable.
    def is_traversable(self, x, y):
        return self.get(x, y) != OBSTACLE

# Return the neighbors of a case. 
# 'diagonal' enables by default moving in diagonal through the grid.
    def neighbors(self, xy, diagonal=True):
    
        x, y = xy

        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return []
        
        neighbors = []
        
        for i in range(3):
            for j in range(3):
                
                nx = x + i - 1
                ny = y + j - 1
                
                if nx >= 0 and ny >= 0 \
                and nx < self.width and ny < self.height \
                and self.is_traversable(nx, ny) \
                and (nx != x or ny != y) \
                and (diagonal or (nx == x or ny == y)): # this is to disable diagonal movement
                    neighbors.append((nx, ny))
        
        return neighbors

    # Prints the grid on the screen.
    # solution : an array figuring a path, to show the results of the shortest-path algorithm.
    def print(self, solution=[]):
        for i in range(self.width):
            for j in range(self.height):
                cg = ' '
                val = self.get(i, j)
                if val == OBSTACLE:
                    cg = '+'
                elif (i,j) in solution:
                    cg = '#'
                elif val != 0:
                    cg = '*'
                printw(cg + " ")
            print("")

    def fill_random(self):
        for i in range(self.width * self.height):
            val = randint(1, 10)
            if val < 4:
                self.set(int(i%self.width), int(i/self.width), OBSTACLE)

    def save_to_file(self, filepath):
        with open(filepath, "w") as ouf:
            ouf.write("%d %d\n" % (self.width, self.height))
            for i in range(self.width):
                for j in range(self.height):
                    val = self.get(i, j)
                    if val == OBSTACLE:
                        ouf.write('1')
                    else:
                        ouf.write('0')
                ouf.write("\n")
            
    def load_from_file(self, filepath):
        gr = Grid(0, 0)
        header = True
        i = 0
        with open(filepath) as inf:
            for line in inf:
                if header:
                    header = False
                    splits = line.split(' ')
                    gr.width, gr.height = int(splits[0]), int(splits[1])
                    gr.generate()
                else:
                    j = 0
                    for c in line:
                        gr.set(i, j, OBSTACLE if c == '1' else EMPTY)
                        j = j + 1
                    i = i + 1
        self.width, self.height, self.data = gr.width, gr.height, gr.data
    def reset(self):
        self.generate()