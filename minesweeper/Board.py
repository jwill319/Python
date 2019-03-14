from tkinter import *
from Tile import Tile
from random import uniform
import pprint

class Board(object):
    def __init__(self, root, rows, cols):
        self.rows = rows
        self.cols = cols

        root.title("Minesweeper Demo")
        root.geometry("400x400")
        #root.resizable(0,0)
        self.root = root
        self.root.grid()

        self.frame = Frame(root, height = 400, width = 400)
        self.frame.grid()

        self.tiles = dict()
        
        self.isGameOver = False
    
        self.setup(self.frame)

    def setup(self, frame):
        tileSize = frame.winfo_height() // self.rows
    
        for y in range(self.rows):
            for x in range(self.cols):
                tile = Tile(frame, y, x, tileSize, uniform(0,1) < 0.20)
                self.tiles[(x,y)] = tile
                
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
        
def main():
    root = Tk()
    game = Board(root, 10, 10)
    root.mainloop()

if __name__ == "__main__":
    main()
