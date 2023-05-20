import random

computer_guess = random.randint(1, 100)

is_guess_right = False
while not is_guess_right:
    player_guess = input("Guess the number (1-100): ")

    if not player_guess.isdigit():
        print("Invalit Input. Try again...")
        continue

    player_guess = int(player_guess)
    if player_guess == computer_guess:
        print("You win!")
        is_guess_right = True
        break
    elif player_guess < computer_guess:
        print("Too low!")
    else:
        print("Too high!")

