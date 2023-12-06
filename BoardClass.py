from DominoClass import Domino

import numpy as np

class Board:
    shape = (50,50,2)
    board = np.empty(shape, dtype=int)
    board[:][:][:] = -1
    newshape = (50,50,3)
    board_Spots = np.empty(newshape, dtype=int)
    board_Spots[:][:][:] = -1
    Dom_Count = 0

    
    def __init__(self):
        pass
    
    def PlaceTile(self, package, num): # [dom, cord]
       
        if (self.Dom_Count == 0):
            self.PlaceInitial(package[0])
        else:
            if (package[0].is_Horizontal == True):
                #print(package[1][1])
                self.board[package[1][0],package[1][1],0] = num
                if (num == package[0].leftSide):
                    self.board[package[1][0],package[1][1],0] = package[0].rightSide
                else:
                    self.board[package[1][0],package[1][1]-1,0] = package[0].leftSide
            self.UpdateBoardSpots(package[1][0],package[1][1],self.Dom_Count)
            self.UpdateBoardSpots(package[1][0],package[1][1]-1, self.Dom_Count)
            self.Dom_Count += 1
        

    def PlaceInitial(self, dom): #SetPosition(self, is_horizontal, leftOtop, RightObottom):
        self.board[23,23,0] = dom.leftSide
        self.board[23,24,0] = dom.rightSide
        self.board[23,23,1] = self.Dom_Count
        self.board[23,24,1] = self.Dom_Count
        self.UpdateBoardSpots(23,23,0)
        self.UpdateBoardSpots(23,24,0)
        self.Dom_Count += 1
        
        return

        
    def UpdateBoardSpots(self, leftCord,rightCord, Dom_Num): #[[x, y],[x, y]]
        value = self.board[leftCord,rightCord, 0]   
        #print(value)    
        
        
        up_cord = [leftCord-1,rightCord]
        left_cord = [leftCord,rightCord-1]
        right_cord = [leftCord,rightCord+1]
        down_cord = [leftCord+1,rightCord]
        cordList = [up_cord,right_cord,down_cord,left_cord]
        up = self.board[up_cord[0],up_cord[1],0]
        left = self.board[left_cord[0],left_cord[1],0]
        right = self.board[right_cord[0],right_cord[1],0]
        down = self.board[down_cord[0],down_cord[1],0]
        valList = [up,right,down,left]
        up_dom = self.board[up_cord[0],up_cord[1],1]
        left_dom = self.board[left_cord[0],left_cord[1],1]
        right_dom = self.board[right_cord[0],right_cord[1],1]
        down_dom = self.board[down_cord[0],down_cord[1],1]
        DomList = [up_dom,right_dom,down_dom,left_dom]

        for i in range(4):
            #print(i)
            if ((valList[i] != -1)):
                if (self.board[cordList[i][0],cordList[i][1],1] == Dom_Num):
                    self.board_Spots[cordList[i][0],cordList[i][1],0] = 9
                    continue
            self.board_Spots[cordList[i][0],cordList[i][1],0] = value
            if (i == 0 or i == 2):
                self.board_Spots[cordList[i][0],cordList[i][1],1] =  100 #   "V"
            else:
                self.board_Spots[cordList[i][0],cordList[i][1],1] =  200 #   "H"
            if (i == 0 or i == 2): 
               self.board_Spots[cordList[i][0],cordList[i][1],2] =  20  #   "D"
            else:
               self.board_Spots[cordList[i][0],cordList[i][1],2] =  10  #   "S"
               
        #self.PrintBoard()
                


    def PrintBoard(self):
        for x in range(len(self.board)):
            print("")
            for y in range(len(self.board[x])):
                if (self.board_Spots[x,y,0] == -1):
                    print(".", end="")
                else:
                    print(f"{self.board_Spots[x,y,0]}",end="")
        print("\n")

    def CheckPlacement(self, singles, doubles):
        singleList = []
        doubleList = []
        for y in range(len(self.board_Spots)):
            for x in range(len(self.board_Spots)):
                if ((self.board_Spots[y][x][0] >= 0) and (self.board_Spots[y][x][0] < 7)):
                    if (self.board_Spots[y][x][2] == 20):
                        self.board_Spots[y][x][1] = y
                        self.board_Spots[y][x][2] = x
                        doubleList.append(self.board_Spots[y][x])
                        
                    else:
                        self.board_Spots[y][x][1] = y
                        self.board_Spots[y][x][2] = x
                        singleList.append(self.board_Spots[y][x])
        if ((len(singleList)!= 0) and (len(singles)!= 0)):
            for doms in singles:
                for nums in singleList:
                    if (nums[0] == doms.rightSide):
                        #print("Found Match")
                        doms.is_Horizontal = False
                        self.PlaceTile([doms, nums], doms.rightSide)
                    elif (nums[0] == doms.leftSide):
                        doms.is_Horizontal = False
                        #print("Found Match")
                        self.PlaceTile([doms, nums], doms.leftSide)
        elif ((len(doubleList)!= 0) and (len(doubles)!= 0)):
            for doms in doubles:
                for nums in doubleList:
                    if (nums[0] == doms.rightSide):
                        doms.is_Horizontal = True
                        #print("Found Match")
                        self.PlaceTile([doms, nums], doms.leftSide)
        else:
            return -1
                    