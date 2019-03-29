import sys
from tkinter import *
from tkinter import messagebox
from NumTile import NumTile
from Bomb import Bomb
from random import uniform, randrange

class Board(object):
    
    def __init__(self, root, rows, cols):
        self.rows = rows
        self.cols = cols

        winSize = rows * 26
        
        root.title("Minesweeper Demo")
        root.geometry(f"{winSize}x{winSize}")
        root.resizable(0,0)
        self.root = root
        self.root.grid()
        self.frame = Frame(root)
        self.frame.grid(row = 0, column = 0)
       
        self.setup(self.frame)

        self.update()

    def setup(self, frame):
        self.isGameOver = False
        self.isGameWon = False
        self.tiles = dict()
        self.bombs = set()
        
        self.totalBombs = 40

        for i in range(self.totalBombs):
            x = randrange(0, self.cols)
            y = randrange(0, self.rows)
            tile = Bomb(frame, y, x)
            self.bombs.add(tile)
            self.tiles[(x, y)] = tile

        for y in range(self.rows):
            for x in range(self.cols):
                try:
                    validKey = self.tiles[(x, y)]
                except:
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

    def reset(self):
        self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.grid(row = 0, column = 0)
        self.setup(self.frame)
        
    def checkGameOver(self):
        for tile in self.bombs:
            if tile.isRevealed:
                self.isGameOver = True
                return True
        return False  
    
    def checkGameWon(self):
        for tile in self.bombs:
            if not tile.isFlagged:
                return False;
        self.isGameWon = True
        return True
        
    def update(self):
        if self.checkGameOver() or self.checkGameWon():
            for tile in self.tiles.values():
                tile.button.configure(state = "disabled")
            endState = "Congrats! You won!" if self.isGameWon else "Sorry! You lost!"
            result = messagebox.askyesno("Game End", "%s Care to play again?" % endState)
            if result:
                self.reset()
                self.update()
            else:
                sys.exit(0)
        else:
            self.root.after(500, self.update)
