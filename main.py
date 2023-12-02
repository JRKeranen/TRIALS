#main
from Pile import Pile
from Player import Player
from BoardClass import Board

if __name__ == "__main__":

    bonePit = Pile()
    p1 = Player(1)
    p2 = Player(2)
    p1.goFirstValue = bonePit.GoFirstDraw()
    p2.goFirstValue = bonePit.GoFirstDraw()
    
    b1 = Board()
    b1.PrintBoard()
    if p1.goFirstValue > p2.goFirstValue:
        print("p1 Goes first \n")
    else:
        print("p2 goes first \n")

    print(f"can i pick? - {bonePit.CanPick()}\n")
    print(f"num tiles - {bonePit.numTiles}")
    print(f"bonepit size - {bonePit.numTiles}")

    x = bonePit.Pick()
    y = bonePit.Pick()
    b1.PlaceInitial(x)
    b1.PlaceTest(y)
    b1.PrintBoard()
    p1.AddToHand(x)
    p1.AddToHand(bonePit.Pick())
    p1.AddToHand(bonePit.Pick())
    p1.AddToHand(bonePit.Pick())
    p1.AddToHand(bonePit.Pick())
    p1.AddToHand(bonePit.Pick())
    print(f"p1 hand size before tile played - {p1.handSize}")
    print(f"p1 hand points = {p1.CalcPoints()}")
    p1.PlayTile(x)
    print(f"p1 hand size after tile played - {p1.handSize}")
    print(f"p1 hand points = {p1.CalcPoints()}")
    print(f"bonepit size - {bonePit.numTiles}")