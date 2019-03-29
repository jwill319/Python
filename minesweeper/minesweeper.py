from tkinter import *
import sys
from Board import Board

def main():
    root = Tk()
    game = Board(root, 16, 16)     
    root.mainloop()

if __name__ == "__main__":
    main()
