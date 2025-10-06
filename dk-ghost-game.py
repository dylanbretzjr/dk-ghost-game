# Ghost Game

from random import randint

print("Ghost Game")

play_again = "Y"

while play_again.upper() == "Y":
    feeling_brave = True
    score = 0

    while feeling_brave:
        ghost_door = randint(1, 3)
        print("Three doors ahead ...")
        print("A ghost behind one.")
        print("Which door do you open?")
        door = input("1, 2, or 3? ")

        if door not in ["1", "2", "3"]:
            print("Oops! That's not a choice.")
            continue

        door_num = int(door)

        if door_num == ghost_door:
            print("GHOST!")
            feeling_brave = False
        else:
            print("No ghost!")
            print("You enter the next room.")
            score += 1

    print("Run away!")
    print("Game over! You scored", score)
    play_again = input("Do you want to play again? (Y or N) ")

print("Goodbye!")
