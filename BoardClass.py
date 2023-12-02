from DominoClass import Domino

import numpy as np

class Board:
    rows, cols = (50, 50)
    board = np.full((50, 50), ".")
    boardWTiles = np.full((50, 50), ".")

    
    def __init__(self):
        pass
    
    def PlaceInitial(self, dom): #SetPosition(self, is_horizontal, leftOtop, RightObottom):
        dom.SetPosition(False, dom.GetLeftSide(), dom.GetRightSide())
        print(self.boardWTiles[24][24])
        self.DrawBoard(dom, [23,23])
        #self.boardWTiles[24,24] = -1
        pass

    def PlaceTest(self, dom): #SetPosition(self, is_horizontal, leftOtop, RightObottom):
        dom.SetPosition(True, dom.GetLeftSide(), dom.GetRightSide())
        self.DrawBoard(dom, [26,23])
        #self.boardWTiles[24,24] = -1
        pass

    def PrintBoard(self):
        for x in range(len(self.board)):
            print("")
            for y in range(len(self.board[x])):
                print(f"{self.boardWTiles[x,y]}", end="")
        print("\n")

    def DrawBoard(self, dom, xy): # xy Cordinate is bottom left where you want to write domino
        Horizonal = dom.is_Horizontal
        if (Horizonal == True):
            self.boardWTiles[xy[1], xy[0]] = f"|"
            self.boardWTiles[(xy[1]), xy[0]+1] = f"`"
            self.boardWTiles[(xy[1]), xy[0]+2] = f"|"

            self.boardWTiles[xy[1]+1, xy[0]] = f"{dom.Left}"
            self.boardWTiles[(xy[1]+1), xy[0]+1] = "|"
            self.boardWTiles[(xy[1]+1), xy[0]+2] = f"{dom.Right}"

            self.boardWTiles[xy[1]+2, xy[0]] = "|"
            self.boardWTiles[(xy[1]+2), xy[0]+1] = f"_"
            self.boardWTiles[(xy[1]+2), xy[0]+2] = f"|"
        else:
            self.boardWTiles[xy[1], xy[0]] = f"|"
            self.boardWTiles[(xy[1]), xy[0]+1] = f"{dom.Top}"
            self.boardWTiles[(xy[1]), xy[0]+2] = f"|"

            self.boardWTiles[xy[1]+1, xy[0]] = f"|"
            self.boardWTiles[(xy[1]+1), xy[0]+1] = "-"
            self.boardWTiles[(xy[1]+1), xy[0]+2] = f"|"

            self.boardWTiles[xy[1]+2, xy[0]] = "|"
            self.boardWTiles[(xy[1]+2), xy[0]+1] = f"{dom.Bottom}|"
            self.boardWTiles[(xy[1]+2), xy[0]+2] = f"|"
            