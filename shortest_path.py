
# Jocelyn Vernay, 2017
# This program implements a shortest-path algorithm.

from simple_grid import Grid

from random import randint
import sys

# Print something without EOL.
def printw(strs):
    sys.stdout.write(str(strs))
    sys.stdout.flush()
    
# Print an array, although this is useless, str() does the same
def printArray(array):
    printw("[")
    for i in range(len(array)):
        if i != 0:
            printw(", ")
        printw(array[i])
    print("]")

# A node of the graph that will be traversed
class Node:
    idd = 0
    def __init__(self):
        self.children = []
        self.id = Node.idd
        Node.idd = Node.idd + 1
        
    def __str__(self):
        return chr(self.id + 65)
        
    def child(i):
        if i < 0 or i >= len(self.children):
            return None
        else:
            return self.children[i]
        
    def appendChild(self, ch):
        self.children.append(ch)
        
    def appendChildren(self, ch):
        self.children.extend(ch)
    
# Computes the distance between two nodes.
# As we are in a grid, it is always equal to 1.    
def compute_distance(a, b):
    return 1
    #ee = a[1] - b[1] + a[0] - b[0]
    #ee = abs(ee)
    #return ee

# Not sure what that is ... 
"""
def shortestPath(src, dest):
    if src == None or dest == None:
        return []
    
    # instead of using nodes, just use tuples of coordinates
    open_nodes = [src]
    explored_nodes = []
    parents = {}
    #parents[src] = (None, 0)
    
    while len(open_nodes) > 0:
        node = open_nodes.pop(0)
        if node in explored_nodes:
            continue
        elif node == dest:
            printw("Found it ! Retrieving path ")
            return retrievePath(node, parents)
        else:
            # and here, use a function to retrieve the traversable neighbors
            for c in node.children:
                open_nodes.append(c)
                distance = computeDistance(node, c)
                if c not in parents or (c in parents and parents[c][1] > distance):
                    parents[c] = (node, distance)
        explored_nodes.append(node)
    
    return [], -1
"""

# Retrieve the path to a node through its parents.
# 'i' is for tests I suppose.
def retrieve_path(src, dest, parents):
    
    i = 100
    
    path = []
    node = dest
    distance = 0
    while node != None and i > 0:
        #i = i - 1
        #if (i%10 == 0):
        #    printw(".")
        path.append(node)
        
        if node == src:
            #path.append(node)
            node = None
        elif node in parents:
            pair = parents[node]
            parents.pop(node)
            node = pair[0]
            distance = distance + pair[1]
        else:
            node = None
        #print(path)
        
    #print("")
    #if i == 0:
    #    print("out of work")
    return path[::-1], distance

##############################################

# You can choose to allow diagonal movement or not.
def shortest_path_in_grid(src, dest, grid, allowDiagonalMovement=True):
    if src == None or dest == None:
        return [], -1
        
    #print(str(src) + " > " + str(dest))
    
    # instead of using nodes, just use tuples of coordinates
    open_nodes = [src]
    explored_nodes = []
    parents = {}
    
    while len(open_nodes) > 0:
        node = open_nodes.pop(0)
        
        if node in explored_nodes:
            #print(str(node) + " has already been explored")
            continue
        elif node == dest:
            # and here, use a function to retrieve the traversable neighbors
            return retrieve_path(src, node, parents)
        else:
            for c in grid.neighbors(node, diagonal=allowDiagonalMovement):
                open_nodes.append(c)
                distance = compute_distance(node, c)
                if c not in parents or (c in parents and parents[c][1] > distance) and c != src:
                    parents[c] = (node, distance)
                    
        explored_nodes.append(node)
        #print(parents)
    
    return [], -1

if __name__ == '__main__': 
    #gr = loadGrid("witcher.txt") 
    gr = Grid(0, 0)
    gr.load_from_file("witcher.txt")
    #fillRandom(gr)

    s = (0, 0)
    d = (gr.width - 1, gr.height - 1)
    spath, length = shortest_path_in_grid(s, d, gr)
    print(spath)
    gr.print(spath)
    
    print("REVERSE:")
    spath, length = shortest_path_in_grid(d, s, gr)
    print(spath)
    gr.print(spath)
    #saveGrid(gr, "witcher.txt")

    #printGrid(loadGrid("witcher.txt"))