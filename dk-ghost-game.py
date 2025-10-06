# Ghost Game

from random import randint, choice

safe_messages = [
    "\nYou sneak through safely...",
    "\nThe coast is clear!",
    "\nPhew! No ghost this time.",
    "\nYour heart’s racing... but nothing jumps out."
]


def play_round():
    """Play one round of the ghost game and return the score."""
    feeling_brave = True
    score = 0

    while feeling_brave:
        ghost_door = randint(1, 3)
        print("\nThree doors ahead ...\nA ghost behind one.\nWhich door do you open?")
        door = input("1, 2, or 3?\n")

        if door not in ["1", "2", "3"]:
            print("\nOops! That's not a choice.")
            continue

        door_num = int(door)
        
        if door_num == ghost_door:
            print("\nGHOST! 👻")
            feeling_brave = False
        else:
            print(choice(safe_messages))
            score += 1

    print("\nRun away!\n")
    print(f"Game over! You scored {score}.")
    return score


def ask_replay():
    """Ask the user if they want to play again, returning True or False."""
    
    while True:
        replay = input("\nDo you want to play again? (Y/N)\n").strip().upper()
        
        if replay == "Y":
            return True
        elif replay == "N":
            return False
        else:
            print("\nPlease enter Y or N.")


def main():
    """Main game loop."""
    print("Welcome to the Ghost Game! 👻")
    high_score = 0

    while True:
        current_score = play_round()

        if current_score > high_score:
            high_score = current_score
            print(f"\n🎉🎉🎉 New high score: {high_score}! 🎉🎉🎉")
        else:
            print(f"\nYour high score is {high_score}.")
        
        if not ask_replay():
            break

    print("\nGoodbye! Thanks for playing!")


if __name__ == "__main__":
    main()
