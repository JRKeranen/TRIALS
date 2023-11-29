import threading
import random
import time

class DominoGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.board = []
        self.players = []
        self.mutex = threading.Lock()
        self.winner = None

        # Initialize players
        for i in range(num_players):
            player = threading.Thread(target=self.play_domino, args=(f"Player {i + 1}",))
            self.players.append(player)

    def start_game(self):
        # Start all player threads
        for player in self.players:
            player.start()

        # Wait for all players to finish
        for player in self.players:
            player.join()

        # Print the winner or declare a tie
        if self.winner:
            print(f"{self.winner} wins!")
        else:
            print("It's a tie!")

    def play_domino(self, player_name):
        while True:
            # Simulate automatic play (random moves)
            move = self.generate_random_move()

            with self.mutex:
                # Perform the move and update the board
                self.board.append((player_name, move))
                print(f"{player_name} plays {move}. Board: {self.board}")

                # Check for a winner or tie
                if len(self.board) >= 6:
                    self.winner = player_name
                    break

            # Introduce a delay to simulate real gameplay
            time.sleep(0.5)

    def generate_random_move(self):
        # Simulate a random domino move
        return (random.randint(0, 6), random.randint(0, 6))

# Create a DominoGame with 3 players
domino_game = DominoGame(num_players=3)

# Start the game
domino_game.start_game()
