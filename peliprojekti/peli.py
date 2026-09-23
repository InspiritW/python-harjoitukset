# 18:15 done, 01.09.2026
# 3. 18:24 done, 10.09.2026
# 4 and # 5 16:02 done, 23.09.2026

import json

from item import Potion
from room import Room
from player import Player

SHOP_POTIONS = [
    Potion("Hint Potion", 1, "Gives you an extra hint!"),
    Potion("Answer Potion", 3, "Gives you the answer!")
]


def give_reward(player, riddle_number, hint_shown):
    reward = 1 if hint_shown else 3
    player.solved.add(riddle_number)
    player.score += reward
    if reward == 1:
        print("Great job! You earned 1 coin!")
    else:
        print(f"Great job! You earned {reward} coins!")


def play_riddle(player, rooms):
    next_riddle = 1
    while next_riddle in player.solved:
        next_riddle += 1

    if next_riddle > len(rooms):
        print("You have solved every riddle!")
        return

    player.move(rooms[next_riddle - 1])
    print(f"Riddle {next_riddle}!")

    if next_riddle == 1:
        play_riddle_1(player)
    elif next_riddle == 2:
        play_riddle_2(player)
    elif next_riddle == 3:
        play_riddle_3(player)
    else:
        print("This riddle is not ready yet. More riddles coming soon!")


def play_riddle_1(player):
    print("Digit 1: I am one.")
    print("Digit 2: I am seven more than digit 1.")
    print("Digit 3: I am two less than digit 2.")
    print("Digit 4: I am one less than digit 3.")

    hint_shown = False
    while True:
        user_answer = input("What am i? (write 'hint' if you want a hint) ")
        if user_answer.strip().lower() in ("hint", "hint?"):
            print("Hint, The year a major war ended")
            hint_shown = True
        elif user_answer.strip() != "1865":
            print("Wrong answer, try again!")
        else:
            give_reward(player, 1, hint_shown)
            break

    next_step = input("Return to menu? enter 1. \nGo to the next riddle? Enter 2!\nSelect 1 or 2! >")
    if next_step == "2":
        print("More riddles coming soon!")


def play_riddle_2(player):
    print("I am the beginning of everything, the end of time and space.")
    print("I am the beginning of every end, and the end of every place.")

    hint_shown = False
    while True:
        user_answer = input("What am i? (write 'hint' if you want a hint) ")
        if user_answer.strip().lower() in ("hint", "hint?"):
            print("Hint, look at the letters, not the things")
            hint_shown = True
        elif user_answer.strip().lower() != "e":
            print("Wrong answer, try again!")
        else:
            give_reward(player, 2, hint_shown)
            break

    next_step = input("Return to menu? enter 1. \nGo to the next riddle? Enter 2!\nSelect 1 or 2! >")
    if next_step == "2":
        print("More riddles coming soon!")


def play_riddle_3(player):
    print("I know a word of letters three. Add two, and fewer there will be.")

    hint_shown = False
    while True:
        user_answer = input("What am i? (write 'hint' if you want a hint) ")
        if user_answer.strip().lower() in ("hint", "hint?"):
            print("Hint, the answer is hiding inside the word 'fewer'")
            hint_shown = True
        elif user_answer.strip().lower() != "few":
            print("Wrong answer, try again!")
        else:
            give_reward(player, 3, hint_shown)
            break

    next_step = input("Return to menu? enter 1. \nGo to the next riddle? Enter 2!\nSelect 1 or 2! >")
    if next_step == "2":
        print("More riddles coming soon!")


def show_progress(player):
    print("Here you can see which riddles you have completed. ")
    if 1 in player.solved:
        print("Riddle 1 is completed!")
    else:
        print("Riddle 1 is not completed!")
    if 2 in player.solved:
        print("Riddle 2 is completed!")
    else:
        print("Riddle 2 is not completed!")
    if 3 in player.solved:
        print("Riddle 3 is completed!")
    else:
        print("Riddle 3 is not completed!")


def shop(player):
    print("Welcome to the shop!")
    print("You can buy potions here that help you in many ways!")

    if player.score == 1:
        print(f"You have {player.score} coin")
    else:
        print(f"You have {player.score} coins")

    for potion_item in SHOP_POTIONS:
        if potion_item.cost <= 1:
            print(f"Potion: {potion_item.name}, costs {potion_item.cost} coin, {potion_item.info}")
        else:
            print(f"Potion: {potion_item.name}, costs {potion_item.cost} coins, {potion_item.info}")

    while True:
        which_potion = input("Which potion do you want to buy? (write 'back' to leave) ")
        if which_potion.lower() == "back":
            return

        potion_selected = None
        for potion_item in SHOP_POTIONS:
            if potion_item.name == which_potion:
                potion_selected = potion_item
        if potion_selected is None:
            print("Non-existant potion selected. Try again.")
            continue

        if player.score < potion_selected.cost:
            print("You cannot afford this.")
            continue

        choise_input = input("You can afford this, do you want to buy it? 1 for yes, 2 for no. ")
        if not choise_input.isdigit():
            print("Non-existant option selected. Try again.")
            continue
        choise = int(choise_input)
        if choise == 1:
            print("Thank you for shoppin!")
            player.score -= potion_selected.cost
            player.items.append(potion_selected)
            return
        elif choise == 2:
            print("Alright.")


def inventory(player):
    print("Welcome to your inventory!")
    print("Here you can view your available potions!")
    for potion in player.items:
        print(f"You have {potion.name}")


def quit_game():
    print("Hope to see you soon!")


def show_text_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Could not find {filename}!")


def save_game(player):
    item_names = []
    for potion in player.items:
        item_names.append(potion.name)

    save_data = {
        "name": player.name,
        "room": player.location.name,
        "score": player.score,
        "items": item_names,
        "solved": sorted(player.solved)
    }

    with open("savegame.json", "w") as file:
        json.dump(save_data, file)


def load_game(rooms):
    try:
        with open("savegame.json", "r") as file:
            save_data = json.load(file)
    except FileNotFoundError:
        return None

    room = rooms[0]
    for saved_room in rooms:
        if saved_room.name == save_data["room"]:
            room = saved_room

    player = Player(save_data["name"], room)
    player.score = save_data["score"]
    player.solved = set(save_data["solved"])

    for item_name in save_data["items"]:
        for potion in SHOP_POTIONS:
            if potion.name == item_name:
                player.items.append(potion)

    return player


def main():
    rooms = [Room("Riddle 1"), Room("Riddle 2"), Room("Riddle 3")]

    show_text_file("intro.txt")
    show_text_file("instructions.txt")

    player = load_game(rooms)
    if player is not None:
        continue_input = input(f"Continue as {player.name}? enter 1 to continue, 2 to start a new game. ")
        if continue_input != "1":
            player = None

    if player is None:
        ask_name = input("What is your name? ")
        ask_age = input("What is your age? ")
        name = ask_name
        age = ask_age
        print(f"{name}, {age}")
        if not age.isdigit():
            print("Age must be a number. Goodbye!")
            return
        age_int = int(age)
        if age_int < 12:
            print("You are underage!")
            return
        player = Player(name, rooms[0])
        print(f"Greetings {name}, Welcome to Codebreaker! ")
    else:
        print(f"Greetings {player.name}, Welcome back to Codebreaker! ")

    while True:
        print("1. Play!")
        print("2. Progress!")
        print("3. Quit Game!")
        print("4. Shop!")
        print("5. Inventory!")
        command = input("Choose option 1-5! ")

        if command == "3":
            save_game(player)
            print("Game saved.")
            quit_game()
            break
        elif command == "1":
            play_riddle(player, rooms)
        elif command == "2":
            show_progress(player)
        elif command == "4":
            shop(player)
        elif command == "5":
            inventory(player)
        elif command not in ("1", "2", "3", "4", "5"):
            print(f"{command} is not a real option!")


if __name__ == "__main__":
    main()
