# BoardClass.py
from DominoClass import Domino
import numpy as np

class Board:
    rows, cols = (50, 50)
    boardWTiles = np.full((50, 50), ".")

    def PlacePiece(self, dom, is_horizontal, xy):
        dom.SetPosition(is_horizontal, dom.GetLeftSide(), dom.GetRightSide())
        self.DrawBoard(dom, xy)

    def PrintBoard(self):
        for x in range(len(self.boardWTiles)):
            print("")
            for y in range(len(self.boardWTiles[x])):
                print(f"{self.boardWTiles[x, y]}", end="")
        print("\n")

    def DrawBoard(self, dom, xy):
        for i in range(3):
            for j in range(3):
                if dom.is_Horizontal:
                    self.boardWTiles[xy[1] + i, xy[0] + j] = self.HorizontalTile(dom, i, j)
                else:
                    self.boardWTiles[xy[1] + i, xy[0] + j] = self.VerticalTile(dom, i, j)

    def HorizontalTile(self, dom, i, j):
        if i == 1 and j == 1:
            return "|"
        elif i == 1:
            return dom.Left if j == 0 else dom.Right
        else:
            return "`" if j == 1 else "_"

    def VerticalTile(self, dom, i, j):
        if j == 1:
            return "-" if i == 1 else dom.Top
        elif j == 0 or j == 2:
            return "|"
        else:
            return dom.Bottom if i == 2 else ""