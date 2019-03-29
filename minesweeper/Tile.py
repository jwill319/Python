# This represents the abstract idea of Tile in Minesweeper
# Version: 1.0
# Author: jwill319

import tkinter as tk
from abc import ABC, abstractmethod

class Tile:
    # Default icon size found in resource folder
    iconsize = 26

    # Constructor for Tile object
    def __init__(self, masterFrame, row, col, isBomb):
        self.x = col
        self.y = row
        self.isBomb = isBomb
        self.isRevealed = False
        self.isFlagged = False

        # Set of surrounding neighbors, initially empty
        self.neighbors = set()
        
        self.master = masterFrame
        self.master.rowconfigure(self.y, minsize = Tile.iconsize)
        self.master.columnconfigure(self.x, minsize = Tile.iconsize)

        # Creates the empty button
        self.button = tk.Button(self.master, text = " ", bg = "white")
        self.button.grid(row = self.y, column = self.x, sticky = tk.N + tk.E + tk.S + tk.W)
        self.button.bind("<Button-1>", self.onLeftClick)
        self.button.bind("<Button-3>", self.onRightClick)

    # Setter to set neighbors from outside class
    def setNeighbors(self, nSet):
        self.neighbors = nSet

    # Event handling depends on whether Tile is a bomb or not
    @abstractmethod
    def onLeftClick(self, event):
        pass

    # Event handling toggles whether or not Tile is flagged or not
    def onRightClick(self, event):
        if self.isFlagged:
            self.button.configure(text = " ", font = ('Times', '10', 'bold'))
            self.isFlagged = False
        else:
            self.button.configure(text = "X", font = ('Times', '10', 'bold'))
            self.isFlagged = True

    # Console representation of a Tile object
    def __repr__(self):
        return "Tile at (x: " + str(self.x) + ", y: " + str(self.y) + ")"
