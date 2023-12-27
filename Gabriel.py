import threading
import random

class Player(threading.Thread):
    def __init__(self, dominoes, lock, player_number, boneyard):
        super().__init__()
        self.dominoes = dominoes
        self.lock = lock
        self.player_number = player_number
        self.boneyard = boneyard

    def run(self):
        while self.dominoes and self.boneyard:
            self.lock.acquire()
            try:
                # Player's game logic
                for i, domino in enumerate(self.dominoes):
                    
                    
                    if domino in board:
                        print("on board")
                        board.append(self.dominoes.pop(i))
                        print(f"Player {self.player_number} played {domino}")
                        break
                else:
                    # If no matching domino in hand, draw from boneyard
                    print("ran")
                    if not self.boneyard:
                        return
                    self.dominoes.append(self.boneyard.pop())
            finally:
                self.lock.release()

# Create a set of dominoes
dominoes = [(i, j) for i in range(7) for j in range(i, 7)]
random.shuffle(dominoes)


# Distribute 7 dominoes to each player and put the rest in the "boneyard"
players_dominoes = [dominoes[i*7:(i+1)*7] for i in range(3)]
boneyard = dominoes[21:]

# Create a lock
lock = threading.Lock()

# Create players, passing the lock to each one
players = [Player(players_dominoes[i], lock, i, boneyard) for i in range(3)]

# The first domino is drawn from the boneyard and placed on the board
board = [boneyard.pop()]

# Start the game
for player in players:
    player.start()

# Wait for all players to finish
for player in players:
    player.join()

# Determine the winner
remaining_counts = [sum(map(sum, player.dominoes)) for player in players]
if all(count == remaining_counts[0] for count in remaining_counts):
    print("The game is a tie.")
else:
    winner = min(range(3), key=lambda i: remaining_counts[i])
    print(f"Player {winner} wins.")