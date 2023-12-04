# this class would store each player information.
from DominoClass import Domino


class Player:
    #Name 
    positionOnTable = 0   # 1,2,3,4    player 2 would be the play clockwise to 1
    #Hand = []
    handSize = 0
    goFirstValue = 0
  # maybe thread
  
    # DONE
    def __init__(self, position, Name):
        self.Name = Name
        self.positionOnTable = position
        self.Hand = []
        self.goFirstValue = 0
        self.CalcHandSize()

    # DONE
    def AddToHand(self, dom):
        self.Hand.append(dom)
        self.CalcHandSize()
    
    # DONE
    def PrintHand(self):
        print("",end="")
        for i in self.Hand:
            print(f" ({i.GetLeftSide()}, {i.GetRightSide()}) ",end="")
        print("")


    # WORKS
    def PlayTile(self, dom):
        x = dom
        self.Hand.remove(dom)
        self.CalcHandSize()
        return x

    # DONE
    def CalcHandSize(self):
        self.handSize = len(self.Hand) 


    # DONE
    def CalcPoints(self):
        sum = 0
        if (self.handSize > 0):
            for i in self.Hand:
                sum += i.GetLeftSide() + i.GetRightSide()
        else:
            return sum
        return sum
    
    def TestPlayTile(self):
        x = self.Hand[0]
        self.Hand.remove(x)
        self.CalcHandSize()
        return x
