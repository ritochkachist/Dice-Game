# 7/20/2023
# Margarita Chistiakova
 
from collections.abc import ValuesView
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, try again.")

max_score = 50
player_scores = [0 for i in range(players)]
current_max_score = 0  # Initializing current_max_score to 0

while current_max_score < max_score:  # Checking against current_max_score
    for player_idx in range(players):
        if player_scores[player_idx] < max_score:
            
            print("\nPlayer number", player_idx + 1, "turn has just started!")
    
            current_score = player_scores[player_idx]
            while True:
                should_roll = input("Would you like to roll (y)? ").lower()
                if should_roll != "y":
                    break
        
                value = roll()
                print("You rolled a:", value)
        
                if value == 1:
                    print("You rolled a 1! Your turn is done!")
                    break
                else:
                    current_score += value
                    print(f"Your score is: {current_score}")
                    player_scores[player_idx] = current_score

                if current_score >= max_score:
                    break

            # Updating current_max_score if the current player's score is greater
            if current_score > current_max_score:
                current_max_score = current_score
    
    # After all players have played, announcing the winner if current_max_score is reached or exceeded
    if current_max_score >= max_score:
        winning_idx = player_scores.index(current_max_score)
        print("\nPlayer number", winning_idx + 1, "is the winner with a score of:", current_max_score)
        break  # Exiting the loop when the winner is found