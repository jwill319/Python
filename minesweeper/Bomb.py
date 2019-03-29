from Tile import Tile
from tkinter import *

class Bomb(Tile):
    def __init__(self, gridFrame, row, col):
        super(Bomb, self).__init__(gridFrame, row, col, True)
        self.icon = PhotoImage(file = "./resources/bomb.png") 
        
    def onLeftClick(self, event):
        if not self.isRevealed:
            self.button.configure(image = self.icon)
            self.isRevealed = True
        
