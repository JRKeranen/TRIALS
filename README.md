Completed Code is on Jack Branch

Variables in the code explaned : ) 


#num_players: This variable represents the number of players in the dominoes game. It is set during the initialization of the DominoGame class.

#board: This list keeps track of the moves played by the players. Each move is represented as a tuple containing the player's name and the domino played.

#players: This list stores the player threads. During the initialization of the DominoGame class, a thread is created for each player and added to this list.

#mutex: This is a threading lock (mutex) used to control access to shared resources, particularly the board and winner variables, ensuring that only one thread can modify them at a time.

#winner: This variable keeps track of the player who wins the game. It starts as None and is updated when a player meets the winning condition.

#play_domino: This method simulates a player's turn in the game. It generates a random move, updates the board, checks for a winner or tie, and introduces a delay to simulate real gameplay.

#generate_random_move: This method generates a random domino move represented as a tuple of two random integers between 0 and 6.

#start_game: This method starts the game by initiating all player threads and waiting for them to finish. It then prints the winner or declares a tie based on the game outcome.


Example of how the code is played to understand it better :

The number of moves in the game is determined by the loop in the play_domino method of the DominoGame class. Let me break down how the moves are generated in this specific example:

Player 1 plays (3, 5).
Player 2 plays (4, 1).
Player 3 plays (1, 0).
Player 1 plays (1, 5).
Player 2 plays (6, 4).
Player 3 plays (0, 4).
Player 1 plays (5, 0).
The loop in the play_domino method continues until the condition len(self.board) >= 5 is satisfied. In this specific example, the loop generates 7 moves before the condition is met, and the game ends. Each move consists of a player playing a domino represented by a pair of numbers.

The moves are generated randomly by the generate_random_move method, which simulates players making random moves. The randomness is introduced by the random.randint(0, 6) function, which generates random integers between 0 and 6 for the two halves of the domino.

If you want to control the number of moves or the winning condition, you can modify the loop condition or introduce additional logic in the code.

Run the code for better undertanding:)







