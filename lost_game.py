import time
import random


def print_delay(story):
    time.sleep(0.1)
    print(story)


def intro(random_planet):
    print_delay(f"You are stranded on the planet {random_planet} all "
                "around you are giant flesh eating sandworms.")
    print_delay("To the north you see a tower in the disstance.")
    print_delay("Next to you is your the wreck of your spaceship.")
    print_delay("The only thing you've got on you is a hoverboard "
                "without a battery.")


def check_input(prompt, option1, option2):
    while True:
        choice = input(prompt).upper()
        if option1 in choice:
            return option1
        elif option2 in choice:
            return option2
        else:
            print_delay("Please try again.")


def game_prompt(items):
    print_delay("Enter A to go to the tower.")
    print_delay("Enter B to look inside the wreck.")
    print_delay("What would you like to do?")
    choice = check_input("(Please enter A or B.)\n", "A", "B")
    if choice == "A":
        tower(items)
    elif choice == "B":
        wreck(items)
    else:
        game_prompt(items)


def tower(items):
    if "hoverboard" in items:
        print_delay("You reach the tower and there is a functioning "
                    "rescue portal at the top.")
        print_delay("You enter the coordinates to you planet.")
        print_delay("Congratulations! You have completed the game.")
        play_again()
    else:
        print_delay("You run towards the tower as fast as you can.")
        print_delay("Halfway you can feel the ground shacking.")
        print_delay("Would you like to turn around?")
        choice = check_input("(yes / no)\n", "YES", "NO")
        if choice == "YES":
            print_delay("Ufff! You make it back to the wreck before "
                        "the worm gets you.")
            game_prompt(items)
        elif choice == "NO":
            print_delay("A giant worm pops out from below your feet and "
                        "swallows you as a whole.")
            print_delay("You die. Game Over!")
            play_again()


def wreck(items):
    print_delay("You go into the ship.")
    if "hoverboard" in items:
        print_delay("There's nothing more to find here.")
        print_delay("You leave the wreck.")
        game_prompt(items)
    else:
        print_delay("Inside the wreck you find a battery for you board.")
        print_delay("Now those nasty sandworms can't locate your "
                    "steps anymore and you can safely travel to the tower.")
        print_delay("You leave the wreck.")
        items.append("hoverboard")
        game_prompt(items)


def play_again():
    choice = check_input("Would you like to play again? (yes / no)\n",
                         "YES", "NO")
    if choice == "YES":
        print_delay("The game is restarting ...")
        play_game()
    elif choice == "NO":
        print_delay("Okay CU!")
    else:
        play_again()


def play_game():
    random_planet = random.choice(["Titan", "Callisto"])
    items = []
    intro(random_planet)
    game_prompt(items)


play_game()
