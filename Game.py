from Pile import Pile
from Player import Player,Domino
from BoardClass import Board

class Game:
    #variables
    is_Winner = bool
    num_Players = int
    passes_In_a_Row = int
    Players = []
    BonePit = Pile

    def __init__(self, num_players):
        self.num_Players = num_players
        self.is_Winner = False
        self.BonePit = Pile()
        self.Players = self.CreatePlayers()

    def CreatePlayers(self):
        ListPlayer = Player
        List = []
        for i in range(self.num_Players):
            ListPlayers = Player(i)
            List.append(ListPlayer)
        return List

    def StartGame(self):
        
        # create pile        
        # self.BonePit = Pile()

        # draw_domino take 7 dominos from pile and give to player
        for i in range(len(self.Players)):
            print(f"in index for players{i}")
            self.InitialDraw(i)
            print(self.Players[i].handSize)

        print(f"bone pit has {self.BonePit.numTiles} tiles")
        
        # see who goes first

        # start middle game with player with highest value as first turn
        pass

    def GameInProgress(self):
        # first player picks random tile and adds to board
        
        # go into turn loop
        
        ######## MAIN LOOP ########

        # 1 - check if player has won HasPlayerWon(self)
        #   #if won endgame, no winner? continue
        # 2 - next person turn
        
        #### Can Play Loop ####
        # 1 - check if player can play a tile ------ Need Function --------

        #   # yes? place and go to main loop, and set pass to 0

        #   # No? try draw a tile   
                # cant draw pass, add to numpass in a row
                # can draw? draw and go back to start of can play loop

        # end on pass or place tile and goes back to mainloop
        pass

    
    def HasPlayerWon(self):
        # check if player has 0 tiles
        # check if pass in row == num of players.
        pass # checks if players have one

    def InitialDraw(self, index):
        #pass 7 tiles from BonePit to player hand
        dom = Domino(0,0)
        for i in range(7):
            dom = self.BonePit.Pick()
            if (dom != -1):
                self.Players[index].AddToHand(dom)
            else:
                print("THERE IS ERROR IN INITIALDRAW")
