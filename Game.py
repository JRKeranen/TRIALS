from Pile import Pile,random
from Player import Player,Domino
from TestBoard import Board
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



    def CreatePlayers(self, numplayer):
        ListPlayer = Player
        List = []
        for i in range(numplayer):
            print(i)
            name = input("Input Player Name: ")
            List.append(Player(i, name ))
        return List




    def StartGame(self):
        # create players
        self.Players = self.CreatePlayers(self.num_Players)
        # Get first player
        first = self.GetFirstPlayer()
        # Draw 7 dominos for each player
        self.InitialDraw()
        ########## start middle game with player with highest value as first turn
        
        threadList = []
        for player in self.Players:
            threadList.append(threading.Thread(target=self.GameInProgress, args=[first]))
        for t in threadList:
            t.start()
        #self.GameInProgress(first)

    def test2(self):
        self.data_Lock.acquire()
        print("sleeping for 2")
        time.sleep(2)
        print("slept")
        self.data_Lock.release()



    def GameInProgress(self, firstPlayer):
        # first player picks random tile and adds to board
        Current_Turn = firstPlayer
        self.Players[Current_Turn].TestPlayTile()
        self.Players[Current_Turn].PrintHand()
        ######## MAIN LOOP ########
        while self.in_Progress is True:
            self.data_Lock.acquire()
            # 1 checks for winner
            if (self.HasPlayerWon() != -1):
                self.PrintWinner(self.HasPlayerWon())
                self.in_Progress = False
                self.data_Lock.release()
                break
            # 2 - next person turn
            Current_Turn = self.ChangeTurn(Current_Turn)
            #### Can Play Loop ####
            Has_Chosen_Tile = False
            for i in range(2):
                # Check if player can play tile
                if (self.CanPlaceTile() == True):
                    self.Players[Current_Turn].TestPlayTile()
                    print(f"{self.Players[Current_Turn].Name} placed a tile")
                    self.passes_In_a_Row = 0
                    self.data_Lock.release()
                    break
                # check if already grabbed tile
                if (Has_Chosen_Tile == True):
                    self.passes_In_a_Row += 1
                    print(f"{self.Players[Current_Turn].Name} Choose a tile, but couold not place it")
                    self.data_Lock.release()
                    break
                # check if player can pick
                if(self.BonePit.CanPick() == True):
                    self.Players[Current_Turn].AddToHand(self.BonePit.Pick())
                    Has_Chosen_Tile = True
                    print(f"{self.Players[Current_Turn].Name} Choosen a Tile")
                else:
                    self.passes_In_a_Row += 1
                    print(f"{self.Players[Current_Turn].Name} Player passed because it could not pick")
                    self.data_Lock.release()
                    break

    


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
    



    def ChangeTurn(self, CurrentTurn):
        CurrentTurn += 1
        if (CurrentTurn >= self.num_Players):
            return 0
        return CurrentTurn


        


    def InitialDraw(self):
        #pass 7 tiles from BonePit to player hand
        for player in self.Players:
            print(f"---- Player {player.Name} {player.positionOnTable}\n")
            for i in range(7):
                fillerDom = self.BonePit.Pick()
                player.AddToHand(fillerDom)
        for player in self.Players:
            print(f"{player.Name} {player.positionOnTable}")
            player.PrintHand()
            print("")



    ####### NEED TO FINISH ######
    def CanPlaceTile(self):
        #pass 7 tiles from BonePit to player hand
        x = random.randint(0, 3)
        return True if (x <=1) else False