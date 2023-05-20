import random

computer_guess = random.randint(1, 100)

print("You have 5 attempts to guess the number!")

attempts_counter = 0
is_guess_right = False

while not is_guess_right:
    player_guess = input("Guess the number (1-100): ")
    if attempts_counter == 5:
        print("You don't have more attempts!")
        break
    attempts_counter += 1

    if not player_guess.isdigit():
        print("Invalit Input. Try again...")
        print(f"You have {5 - attempts_counter} attempts left.")
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
    print(f"You have {5 - attempts_counter} attempts left.")