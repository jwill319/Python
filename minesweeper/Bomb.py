# This represents a Bomb in Minesweeper
# Version: 1.0
# Author: jwill319

from Tile import Tile
import tkinter as tk

class Bomb(Tile):
    
    # Constructor for Bomb
    def __init__(self, gridFrame, row, col):
        super(Bomb, self).__init__(gridFrame, row, col, True)
        self.icon = tk.PhotoImage(file = "./resources/bomb.png") 

    # Reveals the bomb when left clicked
    def onLeftClick(self, event):
        self.button.configure(image = self.icon)
        self.isRevealed = True
            
        
