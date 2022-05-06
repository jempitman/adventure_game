import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro(villain, items):
    print_pause("Following the death of your dear friend and fellow knight "
                "of the round table, King Arthur, you (Sir Lancelot of "
                "Tintagel) are taking a well-earned retirement.\n")
    print_pause("In his last will and testament, King Arthur has left you "
                "a farming village to serve as your pension. You are "
                "currently on your way to take charge of your new village on "
                "foot\n")
    print_pause("On your belt you wear your trusted family sword, "
                "Caliburn.\n")
    print_pause(replace_substring("Whilst walking through a field near the "
                                  "outskirts of the village, you hear that "
                                  "an evil villain is somewhere around here, "
                                  "and has been terrorising the villagers\n",
                                  "villain", villain))
    print_pause("""...\n""")
    print_pause("On your right is a small stream\n")
    print_pause("On your left is a house\n")
    print_pause("Enter 1 to knock on the door of the house\n")
    print_pause("Enter 2 to go down to the small stream\n")
    field(villain, items)


def random_villain():
    villain = random.choice(["dragon", "wizard", "ogre", "fairie"])
    return villain


def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


def field(villain, items):
    print_pause("What would you like to do?\n")
    choice = input("1. Knock on the door of the house?\n"
                   "2. Go down to the stream?\n")

    if choice == "1":
        house(villain, items)
    elif choice == "2":
        stream(villain, items)
    else:
        print_pause("(Please enter 1 or 2)\n")
        field(villain, items)


def house(villain, items):
    print_pause("You knock on the door of the house.\n")
    print_pause(replace_substring("The door opens and out steps the evil "
                                  "villain\n", "villain", villain))
    print_pause(replace_substring("The villain is furious at being woken "
                                  "up and starts attacking you\n", "villain",
                                  villain))
    if "Excalibur" in items:
        print_pause("You feel totally unprepared for this, but suddenly you "
                    "remember the beautiful gift from the Lady of the "
                    "Lake\n")
        fight(villain, items)
    else:
        print_pause("You feel totally underprepared for this, with only your "
                    "old sword Caliburn to defend yourself.\n")
        fight(villain, items)


def fight(villain, items):
    fight_or_flight = input("Would you like to (1) fight or run away (2)?\n")

    if fight_or_flight == "1":
        if "Excalibur" in items:
            print_pause("You unsheath Excalibur and the sun catches the "
                        "blade, throwing off dazzling reflections in all "
                        "direction, as you prepare to attack\n")
            print_pause(replace_substring("The reflection causes the villain "
                                          "to stop for a second.\n", "villain",
                                          villain))
            print_pause(replace_substring("The villain cries out:\n"
                                          "'You wield the magical sword "
                                          "Excalibur!'\n\nand the villain "
                                          "runs away!\n", "villain",
                                          villain))
            print_pause(replace_substring("You have rid the town of the "
                                          "villain. You are victorious!\n",
                                          "villain", villain))
        else:
            print_pause("You attempt to unsheath Caliburn, but rust on the "
                        "blade has caused it to become stuck in its "
                        "scabbard! What a disaster!\n")
            print_pause(replace_substring("You finally unsheath your sword "
                                          "and turn to face the villain\n",
                                          "villain", villain))
            print_pause("However the hesitation has lost you valuable "
                        "seconds you needed to defend yourself.\n")
            print_pause(replace_substring("You fight on valiantly, but "
                                          "ultimately you are no match for "
                                          "the villain\n", "villain",
                                          villain))
            print_pause("You have been defeated!\n")
        play_again()
    elif fight_or_flight == "2":
        print_pause("You turn tail and run as fast as you can!\n")
        print_pause(replace_substring("The villain starts following, "
                                      "but soon gives up the chase as soon "
                                      "as the gap becomes too large.\n",
                                      "villain", villain))
        print_pause("Phew! That was close!\n")
        field(villain, items)
    else:
        print_pause("(Please enter 1 or 2)")
        fight(villain, items)


def stream(villain, items):

    if "Excalibur" in items:
        print_pause("You go back down to the stream and, seeing it "
                    "glistening brightly in the sunshine, think to yourself: "
                    "this will be the ideal place for a spot of fishing!\n")
        print_pause("You drink some of the crystal clear water, and start "
                    "dreaming about the upcoming sunny days fishing in your "
                    "retirement.\n")
    else:
        print_pause("You walk down the gently sloping hill towards the "
                    "stream\n")
        print_pause("Just As you approach the water's edge, a mysterious "
                    "woman rises from the water and suddenly you recognize "
                    "her as the mythical Lady of the Lake!\n")
        print_pause("'Lancelot of Tintagel, for your many years of loyal "
                    "service to King Arthur, I give you his old sword, "
                    "Excalibur! I charge you to use it for the protection of "
                    "the weak and innocent from all forms of tyranny. May it "
                    "serve you well!\n")
        items.append("Excalibur")
        print_pause("You gratefully accept the beautiful gift and discard "
                    "your old rusty sword, Caliburn\n")
    print_pause("You walk back out into the field\n")
    field(villain, items)


def play_again():
    end_game = input("Would you like to play again? (y/n)\n").lower()

    if end_game == "y":
        play_game()
    elif end_game == "n":
        print_pause("Thanks for playing! Until next time, Sir Lancelot!")
    else:
        print_pause("Please enter 'y' or 'n'")
        play_again()


def play_game():
    items = []
    villain = random_villain()
    intro(villain, items)


play_game()
