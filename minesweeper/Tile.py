from tkinter import *
from abc import ABC, abstractmethod

class Tile:
    def __init__(self, gridFrame, row, col, isBomb):
        self.master = gridFrame
        
        self.x = col
        self.y = row
        self.isBomb = isBomb
        self.neighbors = set()

        self.button = Button(self.master, text = "?", bg = "white")
        self.button.grid(row = self.y, column = self.x, sticky = N + S + W + E)                 
        self.button.bind("<Button-1>", self.onLeftClick)
        self.button.bind("<Button-3>", self.onRightClick)

    def setNeighbors(self, nSet):
        self.neighbors = nSet

    @abstractmethod
    def onLeftClick(self, event):
        pass
        
    def onRightClick(self, event):
        print("Flag")

    def __repr__(self):
        return "Tile at (x: " + str(self.x) + ", y: " + str(self.y) + ")"
