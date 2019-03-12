from math import pow, sqrt
from random import uniform

# Representation of a Maze object
#
# Author: jwill319
# Version 2.1

class Maze(object):

    # Representation of a Node utilized by a Maze
    class Node(object):
        
        def __init__(self, row, col, probWall):
            """
                Creates instance of Node.

                row: int row or x position of Node
                col: int column or y position of Node
                probWall: float probability that Node is a wall
                previous: pointer to previous node, important for tracing solution
                color: string containing MazeView color 
            """
            self.row = row
            self.col = col
            self.isWall = True if uniform(0,1) < probWall else False            
            self.previous = "STOP"

            if (not self.isWall):
                self.color = "white"
            else:
                self.color = "black"

    def __init__(self, rows, cols, probWall):
        """
            Creates instance of Maze.
            
            rows: int total amount of rows
            col: int total amount of columns
            grid: 2D Array containing instances of Node
            START: Entrance Node
            END: Goal Node
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[self.Node(i,j, probWall) for j in range(cols)] for i in range(rows)]
        self.START = self.grid[0][0]
        self.START.isWall = False
        self.START.color = "red"
        self.END = self.grid[self.rows - 1][self.cols - 1]
        self.END.isWall = False
        self.END.color = "green"
    
    # Returns node's surrounding neighbors
    def getNeighbors(self, node):
        """Returns a set of all possible neighbors of given Node"""
        grid = self.grid
        neighbors = set()
        
        if node.row > 0:
            neighbors.add(grid[node.row - 1][node.col])
        if node.row < self.rows - 1:
            neighbors.add(grid[node.row + 1][node.col])
        if node.col > 0:
            neighbors.add(grid[node.row][node.col - 1])
        if node.col < self.cols - 1:
            neighbors.add(grid[node.row][node.col + 1])

        return neighbors

    def pScore(self, node):
        """Progress score calculates the step distance from START."""
        return (node.row - self.START.row) + (node.col - self.START.col)

    def hScore(self, node):
        """Heuristic scores calculates in Euclidian distance from END."""
        return sqrt(pow(self.END.row - node.row, 2) + pow(self.END.col - node.col, 2))
    
    def fScore(self, node):
        """Fitness score calculates the total cost for node."""
        return self.pScore(node) + self.hScore(node)
    
    def aSolve(self):
        """
            Implementation of the A* algorithm.
            Returns Node with previous pointers to solution or None type if no solution. 
        """
        maze = self.grid

        openNodes = [self.START]
        closedNodes = list()

        # Loop until there are no more nodes to evaluate
        while len(openNodes) > 0:

            # Find the lowest cost node in openNodes
            current = openNodes[0]
            for element in openNodes:
                if self.fScore(element) < self.fScore(current):
                    current = element

            # Return if A* reaches END
            if current == self.END:
                return current

            # Update after evaluation
            openNodes.remove(current)
            closedNodes.append(current)

            # Find the lowest cost neighbor
            for neighbor in self.getNeighbors(current):
                # Skip if evaluated before or if neighbor isWall
                if neighbor in closedNodes or neighbor.isWall:
                    continue

                # Represents the next distance farther from START
                # Ensures algorithm never goes back
                nextStep = self.pScore(current) + 1

                # Adds neighbor if unevaluated
                if neighbor not in openNodes:
                    openNodes.append(neighbor)
                # Skip neighbor if neighbor goes backward from END
                elif self.pScore(neighbor) <= nextStep:
                    continue

                # Neighbor is the next best node
                # Appends neighbor to current as the current best path
                neighbor.previous = current

        # Loop finished but did not find solution
        return None
