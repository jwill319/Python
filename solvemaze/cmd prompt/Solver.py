# This is an implementation of a A* algorithm in Python 3.7.2
# @author jwill
# @version 1.0

from math import pow, sqrt
import random

#Class representing an individual cell
class Node:
    probWall = 0.27
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.isWall = (False, True)[random.uniform(0,1) < Node.probWall]      
        self.state = ('_','/')[self.isWall] 
        self.previous = "STOP"

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return self.state

# Class representing the solver
class Solver:  
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[""] * cols for i in range(rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = Node(i, j)

    # Drawing methods for showing to console
    # TODO: Change into GUI or return a picture file
    def show(self):
        for i in self.grid:
            print(i)
        print("\n")

    def drawSolution(self, node):
        while node != "STOP":
            node.state = "@"
            node = node.previous

    def getNeighbors(self, cell):
        grid = self.grid
        row = cell.row
        col = cell.col
        
        neighbors = set()
        if row > 0:
            neighbors.add(grid[row - 1][col])
        if row < self.rows - 1:
            neighbors.add(grid[row + 1][col])
        if col > 0:
            neighbors.add(grid[row][col - 1])
        if col < self.cols - 1:
            neighbors.add(grid[row][col + 1])
       
        return neighbors

    # Important node calculations
    def gScore(self, start, node):
        return (node.row - start.row) + (node.col - start.col)

    def heuristic(self, end, node):
        dist = pow(node.row - end.row, 2) + pow(node.col - end.col, 2)
        return pow(dist, 0.5)

    def fScore(self, start, end, node):
        return self.gScore(start, node) + self.heuristic(node, end)

    # A* Algorithm
    def aSolve(self):      
        # Initializes variables for A*
        maze = self.grid
        START = maze[0][0]
        END = maze[self.rows - 1][self.cols - 1]
        START.isWall = False
        START.state = "S"
        END.isWall = False
        END.state = "#"

        print("Before:\n")
        self.show()

        # Contains node to be evaluated
        openSet = [START]

        # Contains node already evaluated
        closedSet = list()

        while len(openSet) > 0:
            # Find lowest fScore in openSet
            current = openSet[0]
            for element in openSet:
                if self.fScore(START, END, element) < self.fScore(START, END, current):
                    current = element
            
            # Check if we found the end
            if current == END:
                self.drawSolution(current)
                print("End:\n")
                self.show()
                break
            
            # Update openSet and closedSet with evaluated data
            openSet.remove(current)
            
            closedSet.append(current)

            for neighbor in self.getNeighbors(current):
                # Skip if evaluated before or if wall
                if neighbor in closedSet or neighbor.isWall:
                    continue

                nextStep = self.gScore(START, current) + 1

                if neighbor not in openSet:
                    openSet.append(neighbor)
                elif self.gScore(START, neighbor) < nextStep:
                    continue
                
                neighbor.previous = current


        # If we break out of loop without finding end, game over and no solution  
        if len(openSet) == 0:
            print("End:\n")
            self.show()
            print("\nNo Solution")
            
def main():
    solver = Solver(20, 20)
    solver.aSolve()

if __name__ == "__main__":
    main()
