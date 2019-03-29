# This represents a non-bomb Tile in Minesweeper
# Version: 1.0
# Author: jwill319

from Tile import Tile
class NumTile(Tile):

    # Constructor for NumTile    
    def __init__(self, gridFrame, row, col):
        super(NumTile, self).__init__(gridFrame, row, col, False)
        self.bombs = 0

    # Event handling for left click
    def onLeftClick(self, event):
        self.reveal()

    # Reveals the current NumTile
    def reveal(self):
        if not self.isRevealed:
            self.button.configure(text = str(self.bombs), font = ('Times', '10', 'bold'), state = "disabled")
            self.isRevealed = True
            self.revealNeighbors()

    # Reveals neighboring NumTiles if there are no surrounding bombs      
    def revealNeighbors(self):
        if (self.bombs != 0):
            return
        
        for tile in self.neighbors:
            if not tile.isBomb:
                tile.reveal()
                
