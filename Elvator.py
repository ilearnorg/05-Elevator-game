import time
import random


def print_timer(message):
    print(message)
    time.sleep(2)


def welcomeintro():
    print_timer("\nRumor has it that so many Monsters are somewhere around "
                "\nhere, and has been terrifying the nearby village.")
    print_timer("In front of you is a house.")
    print_timer("To your right is a dark cave.")
    print_timer("In your hand you hold your trusty"
                "(but not very ""effective) dagger.")


def cave(pocket, selected, physical):
    if ("sword", "HealthPlus") in pocket:
        print_timer("\nYou peer cautiously into the cave.")
        print_timer("You've been here before, and gotten all"
                    "\nthe good stuff. It's just an empty cave"" now.")
        print_timer("You walk back to the Adventure.")
    else:
        print_timer("\nYou peer cautiously into the cave.")
        print_timer("It turns out to be only a very small cave.")
        print_timer("Your eye catches a glint of metal behind a ""rock.")
        print_timer("You have found the magical Sword of Ogoroth!")
        print_timer("You discard your silly old dagger and take"
                    "the sword with you.")
        pocket.append("sword", "HealthPlus")
    print_timer("\nYou walk back out to the Adventure.")
    Adventure(pocket, selected, physical)


def house(pocket, selected, physical):
    print_timer("\nYou approach the door of the house.")
    print_timer("You are about to knock when the door opens"
                "and out steps a " + selected + ".")
    print_timer("Eep! This is the " + selected + "'s house!")
    print_timer("The " + selected + " attacks you!")

    if "sward" not in pocket:
        print_timer("\nYou feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.\n")
    while True:
        Action_1 = input("\nWould you like to \n (1) fight \n"
                         "(2)run away?\n")
        if Action_1 == "1":
            if "sward" in pocket:
                print_timer("\nAs the " + selected + " moves to attack, "
                            "you unlished your new sword.")
                print_timer("The Sword of Ogoroth shines brightly in your"
                            "\nhand as you brace yourself for the attack.")
                print_timer("But the " + selected + "takes one look at"
                            "your shiny new toy and runs away!")
                print_timer("You have rid the town of the " + selected + "."
                            "You are victorious!")
            else:
                print_timer("\nYou do your best...")
                print_timer("but your dagger is no match"
                            "for the " + selected + ".")
                print_timer("\nYou have been defeated!\n")
            play_again()
            break

        if Action_1 == "2":
            print_timer("\nYou run back into the Adventure. "
                        "\nLuckily, you don't seem to have been ""followed.\n")
            Adventure(pocket, selected, physical)
            break


def the_words(pocket, selected, physical):
    print_timer("\nYou decided to go to the woods.\n")
    print_timer("Nature and was so calm with the wispers of birds"
                "\nwhistling and suddenly " + selected + ".")
    print_timer("Damnn! This is the " + selected + "'s Woods!")
    print_timer("The " + selected + " attacks you!\n")
    if "HealthPlus" not in pocket:
        print_timer("\nYou feel a bit under-prepared for this"
                    "\nbecause you just wanted to feel alive"
                    "in Nature for strength.")
        while True:
            Action_2 = input("Would you like to (1) fight or (2) ""play dead?")
            if Action_2 == "1":
                if "HealthPlus" in pocket:
                    print_timer("\nAs you're very healthey and have"
                                "some Extra health you can try to"
                                "fight your way to freedom!")
                    print_timer("As the " + selected +
                                "moves to attack," "you immdiately"
                                "used your " + physical + "  against it.")
                    print_timer("The Great health you have gives you more"
                                "\nstrength to brace yourself for the attack.")
                    print_timer("But the " + selected + "takes"
                                "one look at the nway you use"
                                " + physical + " "to fight and runs away!")
                    print_timer("You have rid the Woods of the"
                                "" + selected + "."
                                "You are victorious!\n")
                else:
                    print_timer("\nYou do your best...")
                    print_timer("but your " + physical + ""
                                "is no match for the " + selected + ".")
                    print_timer("\nYou have been defeated!\n")
                    print_timer("You have so much injury, cant walk but then "
                                "you crawled back to to get"
                                "healed for strenght.\n")
                play_again()
                break
            if Action_2 == "2":
                print_timer("\nYou played dead and the " + selected + ""
                            "thought you to be really ndead and left"
                            "then you run back into to the filed. "
                            "\nLuckily, you don't seem to have"
                            "been ""followed.\n")
                Adventure(pocket, selected, physical)
                break


def status(pocket, selected, physical):
    print_timer("\nYou decided to Check your status and"
                "\nknow what you have for the adventure.")
    print_timer("this is where you check if you have any"
                "equipments already or not")
    print_timer("Status Loading... ")
    if "sword" in pocket:
        print_timer("\nIs very nice you have a shiny"
                    "Sword with Sharp edges")
        print_timer("This Sword can be used coupled"
                    "with your skill to fight Monsters")
    if "HealthPlus" in pocket:
        print_timer("\nNice you've got a healthplus")
        print_timer("This can healp you Heal when injured ")
    else:
        print_timer("\nNohing in your Bag of goodies"
                    "Go back to the game and you might be, "
                    "to get a sword to fight or Health to.\n")
        Adventure(pocket, selected, physical)


def play_again():
    again = input("\nWould you like to play again? (y/n)").lower()
    if again == "y":
        print_timer("\n\n\nGood choice! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_timer("\n\n\nThanks for playing! See you next time:).\n\n\n")
        exit(0)
    else:
        play_again()


def Adventure(pocket, selected, physical):
    print_timer("\nWhat would you like to do?")
    fate = input(" Enter (1) to peer into the cave\n"
                 "Enter (2) to knock on the door of the houseHouse\n"
                 "Enter (3) to goto the Woods for fresh air\n"
                 "Enter (4) to Check your status\n")
    if fate == '1':
        cave(pocket, selected, physical)
    elif fate == '2':
        house(pocket, selected, physical)
    elif fate == '3':
        the_words(pocket, selected, physical)
    elif fate == '4':
        status(pocket, selected, physical)


def play_game():
    pocket = []
    selected = random.choice(["wicked fairie", "Drakula",
                              "dragon", "troll", "gorgon"])
    physical = random.choice(["Fist", "Combat boots",
                              "a heavy wood", "heavey metal"])
    welcomeintro()
    Adventure(pocket, selected, physical)


play_game()

if __name__ == '__main__':
    play_game()
