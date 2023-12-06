#Domino.py
import random

class Domino: 

    #Variables
    leftSide = 0
    rightSide = 0

    is_Horizontal= True
    Double = False
    

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
    
    
    
    
    
    
    # Domino will have a number passed in for left and right side;
    # The pile class will create the dominos for the pile
    # From the pile class it will pass in correct leftSide and Right side to create all the dominos