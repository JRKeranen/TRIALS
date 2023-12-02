#Pile.py
from DominoClass import Domino, random

class Pile:
    #vaiables
    pile = []
    numTiles = 0
  

    ###### DONE
    def __init__(self):
        # initializes the pile of dominos, 28 total
        for i in range(7):
            for j in range(i, 7):
                self.pile.append(Domino(i,j))
        random.shuffle(self.pile)
        self.CalcTiles()



    ##### DONE
    def CalcTiles(self):   # call this everytime you add or remove a tile
        self.numTiles = len(self.pile)



    ##### DONE
    def CanPick(self):
        return False  if (self.numTiles == 0) else True
  


    ##### DONE
    def Pick(self):      #pick a random domino and removes from pile and returns picked domino
        if (self.CanPick() == False):
            return -1
        else:
            i = random.randint(0, (self.numTiles -1))
            dom = self.pile[i]
            self.pile.remove(dom)
            self.CalcTiles()
            return dom
        



    ##### DONE
    def GoFirstDraw(self):
        if (self.CanPick() == False):
            return -1
        else:
            i = random.randint(0, (self.numTiles -1))
            dom = self.pile[i]
            sum = dom.GetRightSide() + dom.GetLeftSide()
            return sum