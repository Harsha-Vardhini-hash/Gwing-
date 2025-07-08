import random

def intro():
    print("You wake up in a dark dungeon. There are 3 tunnels ahead.")
    print("Choose your path: left / right / straight")

def get_choice():
    choice = input("Your choice: ").lower()
    while choice not in ["left", "right", "straight"]:
        print("Invalid choice. Try again.")
        choice = input("Your choice: ").lower()
    return choice

def encounter():
    outcomes = ["monster", "trap", "treasure", "nothing"]
    return random.choice(outcomes)

def play_game():
    health = 100
    inventory = []

    intro()
    choice = get_choice()

    event = encounter()
    print(f"\nYou walk down the {choice} tunnel and encounter... {event}!")

    if event == "monster":
        print("A monster attacks you! You lose 30 HP.")
        health -= 30
    elif event == "trap":
        print("You fell into a trap! You lose 20 HP.")
        health -= 20
    elif event == "treasure":
        print("You found a healing potion! +20 HP.")
        health += 20
        inventory.append("potion")
    else:
        print("The path is clear... for now.")

    print(f"\nYour current health: {health}")
    print(f"Your inventory: {inventory}")

    if health <= 0:
        print("You died in the dungeon. Game Over.")
    else:
        print("You survived this round! Continue exploring...")

# Start game
play_game()
