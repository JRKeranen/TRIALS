# this class would store each player information.
from DominoClass import Domino


class Player:
    positionOnTable = 0   # 1,2,3,4    player 2 would be the play clockwise to 1
    Hand = []
    handSize = 0
    goFirstValue = 0
  # maybe thread
  
    # DONE
    def __init__(self, position):
        self.position = position
        self.hand = []
        self.goFirstValue = 0
        self.CalcHandSize()


    # DONE
    def AddToHand(self, dom):
        self.Hand.append(dom)
        self.CalcHandSize()


    # WORKS
    def PlayTile(self, dom):
        
        self.Hand.remove(dom)
        self.CalcHandSize()

    # DONE
    def CalcHandSize(self):
        self.handSize = len(self.Hand) 
        print(f"From Player hand length {len(self.Hand)}")


    # DONE
    def CalcPoints(self):
        sum = 0
        if (self.handSize > 0):
            for i in self.Hand:
                sum += i.GetLeftSide() + i.GetRightSide()
        else:
            return sum
        return sum
