from Tile import Tile
class NumTile(Tile):
    #colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#7f00ff", "#000000"]
    
    def __init__(self, gridFrame, row, col):
        super(NumTile, self).__init__(gridFrame, row, col, False)
        self.bombs = 0
        
    def update(self):
        self.button.configure(text = str(self.bombs), font = ('Times', '10', 'bold'), state = "disabled")

    def reveal(self):
        if not self.isRevealed:
            self.button.configure(text = str(self.bombs), font = ('Times', '10', 'bold'), state = "disabled")
            self.isRevealed = True
            self.revealNeighbors()
    
    def onLeftClick(self, event):
        self.reveal()
              
    def revealNeighbors(self):
        if (self.bombs != 0):
            return
        
        for tile in self.neighbors:
            if not tile.isBomb:
                tile.reveal()
                
