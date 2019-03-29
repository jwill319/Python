# This represents the Board containing all Tiles in Minesweeper
# Version: 1.0
# Author: jwill319

import sys
from random import uniform, randrange
import tkinter as tk
from tkinter import messagebox
from NumTile import NumTile
from Bomb import Bomb

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
        self.frame = tk.Frame(root)
        self.frame.grid(row = 0, column = 0)
       
        self.setup(self.frame)

        self.update()

    # Given a new Frame, creates grid of Bombs and NumTiles
    def setup(self, frame):
        self.isGameOver = False
        self.isGameWon = False
        self.tiles = dict()
        self.bombs = set()

        # Assigns Bombs to random coordinates
        self.totalBombs = 40
        for i in range(self.totalBombs):
            x = randrange(0, self.cols)
            y = randrange(0, self.rows)
            tile = Bomb(frame, y, x)
            self.bombs.add(tile)
            self.tiles[(x, y)] = tile

        # Assigns every empty coordinate with a NumTile
        for y in range(self.rows):
            for x in range(self.cols):
                try:
                    validKey = self.tiles[(x, y)]
                except:
                    self.tiles[(x, y)] = NumTile(frame, y, x)

        # Algorithm to find and set every Tile's neighbors    
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

            # If the current Tile is not a bomb, set the number of surrounding bombs here
            if not v.isBomb:
                for neighbor in v.neighbors:
                    if neighbor.isBomb:
                        v.bombs += 1
                        
    # Destroys current Frame and setups another
    def reset(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.grid(row = 0, column = 0)
        self.setup(self.frame)

    # Checks if any bomb is revealed
    def checkGameOver(self):
        for tile in self.bombs:
            if tile.isRevealed:
                self.isGameOver = True
                return True
        return False  

    # Checks if all bombs are flagged
    def checkGameWon(self):
        for tile in self.bombs:
            if not tile.isFlagged:
                return False;
        self.isGameWon = True
        return True

    # Recursive updater for game loop
    # Calls game state checkers
    def update(self):
        if self.checkGameOver() or self.checkGameWon():
            for tile in self.tiles.values():
                tile.button.configure(state = "disabled")
            endState = "You won!" if self.isGameWon else "You lost!"
            result = tk.messagebox.askyesno("Game End", "%s Care to play again?" % endState)
            
            # If player wants to continue, reset the game. Else, quit the application
            if result:
                self.reset()
                self.update()
            else:
                sys.exit(0)
        else:
            self.root.after(500, self.update)
