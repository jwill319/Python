from tkinter import *
from NumTile import NumTile
from Bomb import Bomb
from random import uniform

class Board(object):
    
    def __init__(self, root, rows, cols):
        self.rows = rows
        self.cols = cols
        self.isGameOver = False
        self.tiles = dict()

        winSize = rows * 26
        
        root.title("Minesweeper Demo")
        root.geometry(f"{winSize}x{winSize}")
        root.resizable(0,0)
        self.root = root
        self.root.grid()
        self.frame = Frame(root)
        self.frame.grid(sticky = N + S + W + E)
        
        self.setup(self.frame)

    def setup(self, frame):      
        for y in range(self.rows):
            for x in range(self.cols):
                if uniform(0, 1) < .2:
                    self.tiles[(x, y)] = Bomb(frame, y, x)
                else:
                    self.tiles[(x, y)] = NumTile(frame, y, x)
                
        for k, v in self.tiles.items():
            neighbors = set()
            x, y = k

            for nX in range(x - 1, x + 2):
                for nY in range(y - 1, y + 2):
                    if k != (nX, nY):
                        try:
                            neighbors.add(self.tiles[nX, nY])
                        except:
                            continue

            v.setNeighbors(neighbors)
            
            if not v.isBomb:
                for neighbor in v.neighbors:
                    if neighbor.isBomb:
                        v.bombs += 1
                v.update()
      
def main():
    root = Tk()
    game = Board(root, 16, 16)
    root.mainloop()

if __name__ == "__main__":
    main()
