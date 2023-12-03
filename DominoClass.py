#Domino.py
import random

class Domino: 

    #Variables
    leftSide = 0
    rightSide = 0

    is_Horizontal= True
    Double = False
    Top = -1
    Bottom = -1
    Left = -1
    Right = -1
    topLeftCord = [0,0]
    bottomRightCord = [0,0]
    

    ##### DONE
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide
        Double = False if (leftSide != rightSide) else True
    
    
    ##### DONE
    def GetLeftSide(self):
        return self.leftSide
    
    
    ##### DONE
    def GetRightSide(self):
        return self.rightSide
    
    def SetPosition(self, is_horizontal, leftOtop, RightObottom):
        if (is_horizontal == True):
            self.is_Horizontal = True
            self.Left = leftOtop
            self.Right = RightObottom

        else:
            self.is_Horizontal = False
            self.Top = leftOtop
            self.Bottom = RightObottom
    
    
    
    
    # Domino will have a number passed in for left and right side;
    # The pile class will create the dominos for the pile
    # From the pile class it will pass in correct leftSide and Right side to create all the dominos