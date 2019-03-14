from tkinter import *

class Tile:
    def __init__(self, gridFrame, row, col, size, isBomb):
        self.master = gridFrame
        
        self.x = col
        self.y = row
        self.size = size

        self.isBomb = isBomb
        self.neighbors = set()
        self.state = self.tileState()
    
        self.button = Button(self.master, height = size, width = size, text = self.state)
        self.button.grid(row = self.y, column = self.x)
        self.button.bind("<Button-1>", self.onLeftClick)
        self.button.bind("<Button-3>", self.onRightClick)

    def tileState(self):
        if self.isBomb:
            return "X"
        else:
            numBombs = 0
            for neighbor in self.neighbors:
                if neighbor.isBomb:
                    numBombs += 1
            return numBombs

    def setNeighbors(self, nSet):
        self.neighbors = nSet
        self.state = self.tileState()
        self.button.configure(text = str(self.state))
  
    def onLeftClick(self, event):
        #print("Left Clicked Tile at (" + str(self.x) + ", " + str(self.y) + ")")
        if self.isBomb:
            #TODO Add game over state
            print("BOOM!")
        else:
            print(self.state)
               
    def onRightClick(self, event):
        print("Right Clicked Tile at (" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):
        return "Tile at (x: " + str(self.x) + ", y: " + str(self.y) + ")"
