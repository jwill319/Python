from Maze import Maze
from tkinter import *

# Visual representation of a Maze object described in Maze.py
#
# Author: jwill319
# Version: 2.1
class MazeView(object):
    probWall = 0.25
    
    def __init__(self, root):
        """
            Creates instance of MazeView.

            root: parameter containing Tkinter window
            maze: current instance of Maze
            state: Contains the state of the current maze
            canvas: Canvas containing the grid from self.maze
            userFrame: Frame containing all user input
        """
        root.title("A* Algorithm Demo")
        root.geometry("500x580")
        root.resizable(0,0)
        self.root = root

        self.maze = Maze(20, 20, MazeView.probWall)

        self.state = Label(root, text = "Click \"Generate New Maze\" to Begin")
        self.state.pack()
        
        self.canvas = Canvas(self.root, height = 480, width = 480, borderwidth = 5, bg = "#474861")
        self.canvas.pack()

        self.userFrame = Frame(self.root)
        self.userFrame.pack(side = "bottom")

        self.setup(self.canvas, self.userFrame)
        self.root.update()
        
    def setup(self, canvas, userFrame):
        """ Creates grid view and user input capabilities."""
        self.updateMaze(canvas)

        generate = Button(userFrame, text = "Generate New Maze", pady = 5)
        generate.bind("<Button-1>", self.genMaze)
        generate.pack()
        solve = Button(userFrame, text = "Solve!", pady = 5)
        solve.bind("<Button-1>", self.solveMaze)
        solve.pack()

    def genMaze(self, event):
        """ Generates a new maze instance."""
        self.state.configure(text = "Unsolved")
        self.maze = Maze(20, 20, MazeView.probWall)
        self.updateMaze(self.canvas)

    def updateMaze(self, canvas):
        """ Updates the Canvas dependent on changes to self.maze"""
        rows = self.maze.rows
        cols = self.maze.cols

        bHeight = canvas.winfo_width() / cols
        bWidth = canvas.winfo_height() / rows

        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                color = self.maze.grid[i][j].color                
                canvas.create_rectangle(j * bWidth, i * bHeight, (j + 1) * bWidth, (i + 1) * bHeight, width = 0, fill = color, tag = "node")
    

    def solveMaze(self, event):
        """ Runs A* algorithm and draws solution path, if applicable."""
        endNode = self.maze.aSolve()
        if endNode == None:
            self.state.configure(text = "No Solution", fg = "red")
        else:
            node = endNode
            while node != "STOP":
                node.color = "cyan"
                node = node.previous
                
            self.state.configure(text = "Solved", fg = "green")
            self.updateMaze(self.canvas)
    
def main():
    """ Main method running MazeView object."""
    # Intialize Tkinter screen
    root = Tk()
    view = MazeView(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
