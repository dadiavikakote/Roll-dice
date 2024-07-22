import random


def roll_dice():
    roll = random.randint(1, 6)
    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The number must be between 2 and 4.")
    else:
        print("you must enter a number between 2 and 4.")

player_scores = []

for i in range(players):
    players_scores.append(0)

while max(player_scores) < 40:
    for player_index in range(players):
        print("")
        print("Player number", player_index + 1, "turn has begun!")
        print("Your total score is: ", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (yes)? ").lower()
            if should_roll != "yes":
                break

            value = roll_dice()
            if value == 1:
                print("You rolled a 1! your turn is over!")
                current_score = 0
                print("Your score is:", current_score)
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number ", winning_index + 1, " is the winner with a score of: ", max_score)
