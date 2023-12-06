from Pile import Pile,random
from Player import Player,Domino
from BoardClass import Board
import threading
import time

class Game:
    #variables
    in_Progress = bool
    num_Players = int
    #passes_In_a_Row = int
    Players = []
    BonePit = Pile
    board = Board

    def __init__(self, num_players):
        self.num_Players = num_players
        self.in_Progress = True
        self.BonePit = Pile()
        self.passes_In_a_Row = 0
        self.board = Board()
        self.data_Lock = threading.Lock()
        self.current_Turn = 0




    def StartGame(self):
        # create players
        self.Players = self.CreatePlayers(self.num_Players)
        # Get first player
        self.current_Turn = self.GetFirstPlayer()
        print(f"Player in position {self.current_Turn} has the first turn")
        # Draw 7 dominos for each player
        self.InitialDraw()
        ########## start middle game with player with highest value as first turn
        self.GameInProgress()




    def CreatePlayers(self, numplayer):
        ListPlayer = Player
        List = []
        for i in range(numplayer):
            name = input("Input Player Name: ")
            List.append(Player(i, name ))
        return List
    



    def MainGameLoop(self, player_num, threadNum):
        time.sleep(.5)
        print(f"Main Loop Funtion Initiated for thread {threadNum}")

        while self.in_Progress is True:
            if (self.current_Turn == threadNum):
                self.data_Lock.acquire()
                print(f"Lock Aquired on {threadNum}")
            else:
                time.sleep(.1)
                continue

            # 1 checks for winner
            if (self.HasPlayerWon() != -1):
                self.PrintWinner(self.HasPlayerWon())
                self.in_Progress = False
                self.data_Lock.release()
                self.in_Progress = False
                break

            #### Can Play Loop ####
            Has_Chosen_Tile = False
            for i in range(2):
                # Check if player can play tile
                if (self.CanPlaceTile() == True):
                    #grab the domino to place
                    tile = self.Players[self.current_Turn].TestPlayTile( )
                    #place tile to board
                    print(f"{self.Players[self.current_Turn].Name} placed a tile")
                    self.passes_In_a_Row = 0
                    self.ChangeTurn()
                    self.data_Lock.release()
                    break
                # check if already grabbed tile
                if (Has_Chosen_Tile == True):
                    self.passes_In_a_Row += 1
                    print(f"{self.Players[self.current_Turn].Name} Choose a tile, but couold not place it")
                    self.ChangeTurn()
                    self.data_Lock.release()
                    break
                # check if player can pick
                if(self.BonePit.CanPick() == True):
                    self.Players[self.current_Turn].AddToHand(self.BonePit.Pick())
                    Has_Chosen_Tile = True
                    print(f"{self.Players[self.current_Turn].Name} has Drawn a Tile From the Bone Pit")
                else:
                    self.passes_In_a_Row += 1
                    print(f"{self.Players[self.current_Turn].Name} Player passed because it could not pick")
                    self.ChangeTurn()
                    self.data_Lock.release()
                    break




    def GameInProgress(self):
        # first player picks random tile and adds to board
        dom = self.Players[self.current_Turn].TestPlayTile()
        self.board.PlaceTile([dom,[]], 0)
        self.ChangeTurn()
        #self.Players[self.current_Turn].PrintHand()
        ######## MAIN LOOP ########
        threadList = []
        for player in self.Players:
            #print(player.positionOnTable)
            threadList.append(threading.Thread(target=self.MainGameLoop, args=[player.positionOnTable, player.positionOnTable]))
        for t in threadList:
            #t.daemon = True
            t.start()
           


    


    def HasPlayerWon(self):## if there is a winner, return player position, if no winner return -1
        # check if player has 0 tiles
        for player in self.Players:
            if (player.handSize == 0):
                return player.positionOnTable
        # check if all players have passed 
        if self.passes_In_a_Row == self.num_Players:
            least_points = 100
            player_in_lead = -1
            for player in self.Players:
                if (player.CalcPoints() < least_points):
                    player_in_lead = player.positionOnTable
            return player_in_lead
        else:
            return -1





    def GetFirstPlayer(self):
        for player in self.Players:
            player.goFirstValue = self.BonePit.GoFirstDraw()
        max = 0
        name = ""
        position = -1
        for player in self.Players:
            if (player.goFirstValue > max):
                max = player.goFirstValue
                name = player.Name
                position = player.positionOnTable
            else:
                next
        return position
    



    def PrintWinner(self, position):
        winner = self.Players[position]
        print(f"Player {winner.Name} has won the game with {winner.CalcPoints()} points")
    



    def ChangeTurn(self):
        fillerTurn = self.current_Turn
        fillerTurn += 1
        if (fillerTurn >= self.num_Players):
            self.current_Turn = 0
        else:   
            self.current_Turn = fillerTurn


        


    def InitialDraw(self):
        #pass 7 tiles from BonePit to player hand
        for player in self.Players:
            for i in range(7):
                fillerDom = self.BonePit.Pick()
                player.AddToHand(fillerDom)
        for player in self.Players:
            print(f"{player.Name} Initial Hand")
            player.PrintHand()
            print("")



    ####### NEED TO FINISH ######
    def CanPlaceTile(self):
        singles = self.Players[self.current_Turn].GetSingles()
        doubles = self.Players[self.current_Turn].GetDoubles()
        played = self.board.CheckPlacement(singles, doubles)
        if (played == -1):
            return False
        
        return True