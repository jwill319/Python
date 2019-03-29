from tkinter import *
from abc import ABC, abstractmethod

class Tile:
    iconsize = 26
    
    def __init__(self, masterFrame, row, col, isBomb):
        self.x = col
        self.y = row
        self.isBomb = isBomb
        self.isRevealed = False
        self.isFlagged = False
        self.neighbors = set()

        self.master = masterFrame
        self.master.rowconfigure(self.y, minsize = Tile.iconsize)
        self.master.columnconfigure(self.x, minsize = Tile.iconsize)
    
        self.button = Button(self.master, text = " ", bg = "white")
        self.button.grid(row = self.y, column = self.x, sticky = N + E + S + W)
        self.button.bind("<Button-1>", self.onLeftClick)
        self.button.bind("<Button-3>", self.onRightClick)

    def setNeighbors(self, nSet):
        self.neighbors = nSet

    @abstractmethod
    def onLeftClick(self, event):
        pass
        
    def onRightClick(self, event):
        if self.isFlagged:
            self.button.configure(text = " ", font = ('Times', '10', 'bold'))
            self.isFlagged = False
        else:
            self.button.configure(text = "X", font = ('Times', '10', 'bold'))
            self.isFlagged = True

    def __repr__(self):
        return "Tile at (x: " + str(self.x) + ", y: " + str(self.y) + ")"
