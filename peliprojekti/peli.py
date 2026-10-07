# 18:15 done, 01.09.2026
# 3. 18:24 done, 10.09.2026
# 4 and # 5 16:02 done, 23.09.2026
# projekti valmis 19:39, 07.10.2026

import json
import os

from item import Potion, Scrap
from room import Room
from player import Player

# path to this folder
BASE = os.path.dirname(os.path.abspath(__file__))
SAVE_PATH = os.path.join(BASE, "savegame.json")

# potions sold in the shop
SHOP_POTIONS = [
    Potion("Hint Potion", 1, "Gives you an extra hint!"),
    Potion("Answer Potion", 3, "Gives you the answer!")
]

# scraps that can be recycled
SCRAPS = [
    Scrap("Old Bottle", "glass"),
    Scrap("Tin Can", "metal"),
    Scrap("Newspaper", "paper")
]


# tower rooms
def build_tower_rooms():
    return [
        Room("Attic", SCRAPS[0], "A dusty attic full of old boxes."),
        Room("Basement", SCRAPS[1], "A cold basement with shelves of rusty tools."),
        Room("Garden", SCRAPS[2], "A tower garden where the wind blows paper around.")
    ]


# riddle texts with answers and hints
RIDDLES = [
    {
        "lines": ["Digit 1: I am one.",
                  "Digit 2: I am seven more than digit 1.",
                  "Digit 3: I am two less than digit 2.",
                  "Digit 4: I am one less than digit 3."],
        "answer": "1865",
        "hint": "Hint, The year a major war ended"
    },
    {
        "lines": ["I am the beginning of everything, the end of time and space.",
                  "I am the beginning of every end, and the end of every place."],
        "answer": "e",
        "hint": "Hint, look at the letters, not the things"
    },
    {
        "lines": ["I know a word of letters three. Add two, and fewer there will be."],
        "answer": "few",
        "hint": "Hint, the answer is hiding inside the word 'fewer'"
    }
]


# returns coin or coins depending on the amount
def coins(amount):
    return f"{amount} coin" if amount == 1 else f"{amount} coins"


# gives coins for solving a riddle
def give_reward(player, riddle_number, hint_shown):
    reward = 1 if hint_shown else 3
    player.solved.add(riddle_number)
    player.score += reward
    print(f"Great job! You earned {coins(reward)}!")


# removes a potion from the items
def take_potion(player, potion_name):
    for potion in player.items:
        if potion.name == potion_name:
            player.items.remove(potion)
            return True
    return False


# shows a hint and uses a hint potion if there is one
def use_hint(player, hint_text):
    if take_potion(player, "Hint Potion"):
        print(f"You used your Hint Potion! {hint_text}")
        return False
    print(hint_text)
    return True


# plays the next unsolved riddle
def play_riddle(player, rooms):
    next_riddle = 1
    while next_riddle in player.solved:
        next_riddle += 1

    if next_riddle > len(rooms):
        print("You have solved every riddle!")
        return

    player.move(rooms[next_riddle - 1])
    print(f"Riddle {next_riddle}!")

    if ask_riddle(player, next_riddle):
        clear_screen()
        play_riddle(player, rooms)


# asks one riddle
def ask_riddle(player, number):
    riddle = RIDDLES[number - 1]
    for line in riddle["lines"]:
        print(line)

    hint_shown = False
    while True:
        user_answer = input("What am i? (write 'hint' or 'answer' to use a potion) ").strip().lower()
        if user_answer == "hint":
            hint_shown = use_hint(player, riddle["hint"]) or hint_shown
        elif user_answer == "answer" and take_potion(player, "Answer Potion"):
            print(f"You used your Answer Potion! The answer is {riddle['answer']}.")
            give_reward(player, number, True)
            break
        elif user_answer != riddle["answer"]:
            print("Wrong answer, try again!")
        else:
            give_reward(player, number, hint_shown)
            break

    input("\nPress enter to continue ")
    clear_screen()
    next_step = input("Return to menu? enter 1. \nGo to the next riddle? Enter 2!\nSelect 1 or 2! >")
    return next_step == "2"


# shows solved riddles
def show_progress(player):
    print("Here you can see which riddles you have completed. ")
    for number in range(1, len(RIDDLES) + 1):
        state = "completed" if number in player.solved else "not completed"
        print(f"Riddle {number} is {state}!")


# buy potions
def shop(player):
    print("Welcome to the shop!")
    print("You can buy potions here that help you in many ways!")

    print(f"You have {coins(player.score)}")

    for potion_item in SHOP_POTIONS:
        print(f"Potion: {potion_item.name}, costs {coins(potion_item.cost)}, {potion_item.info}")

    while True:
        which_potion = input("Which potion do you want to buy? (write 'back' to leave) ")
        if which_potion.lower() == "back":
            return

        potion_selected = None
        for potion_item in SHOP_POTIONS:
            if potion_item.name.lower() == which_potion.strip().lower():
                potion_selected = potion_item
        if potion_selected is None:
            print("Non-existent potion selected. Try again.")
            continue

        if player.score < potion_selected.cost:
            print("You cannot afford this.")
            continue

        choice_input = input("You can afford this, do you want to buy it? 1 for yes, 2 for no. ")
        if not choice_input.isdigit():
            print("Non-existent option selected. Try again.")
            continue
        choice = int(choice_input)
        if choice == 1:
            print("Thank you for shopping!")
            player.score -= potion_selected.cost
            player.items.append(potion_selected)
            return
        elif choice == 2:
            print("Alright.")


# shows items
def inventory(player):
    print("Welcome to your inventory!")
    print("Here you can see everything you are carrying!")
    for potion in player.items:
        print(f"You have {potion.name}")


# checks which route is done
def check_route(player):
    if len(player.solved) == 3:
        return "Riddle master"
    names = [item.name for item in player.items]
    if "Hint Potion" in names and "Answer Potion" in names:
        return "Merchant"
    if player.recycled >= 3:
        return "Recycler"
    return None


# opens the door if a route is done
def open_door(player):
    route = check_route(player)
    if route is None:
        print("The tower door is still locked. Solve the riddles, buy both potions or recycle 3 scraps first.")
        return False
    print(f"You used the {route} route and cracked the final code! The tower door opens.")
    print(f"Well done {player.name}!")
    return True


# recycles an item for a coin
def recycle(player):
    if not player.items:
        print("You have nothing to recycle.")
        return
    for number, item in enumerate(player.items, start=1):
        print(f"{number}. {item.name}")
    choice = input("What do you want to recycle? Enter a number (anything else to go back) ")
    if not choice.isdigit() or not 1 <= int(choice) <= len(player.items):
        return
    item = player.items.pop(int(choice) - 1)
    player.score += 1
    if isinstance(item, Scrap):
        player.recycled += 1
        print(f"You recycled the {item.name} ({item.material}) and got 1 coin! Scraps recycled: {player.recycled}/3")
    else:
        print(f"You recycled the {item.name} bottle and got 1 coin back!")


# moves to a tower room and takes the scrap
def explore(player, tower_rooms):
    print("Where do you want to go?")
    for number, room in enumerate(tower_rooms, start=1):
        print(f"{number}. {room.name}")
    choice = input("Enter a number (anything else to go back) ")
    if not choice.isdigit() or not 1 <= int(choice) <= len(tower_rooms):
        return
    room = tower_rooms[int(choice) - 1]
    player.move(room)
    print(f"You enter the {room.name}. {room.description}")
    if room.item is None:
        print("There is nothing left to find here.")
        return
    print(f"You found something: {room.item.name}! Take it to the recycling bin.")
    player.items.append(room.item)
    room.item = None


# asks for the name
def ask_name():
    while True:
        name = input("What is your name? ").strip()
        if name:
            return name
        print("Please type a name")


# asks for the age
def ask_age():
    while True:
        age = input("What is your age? ").strip()
        if age.isascii() and age.isdigit() and 1 <= int(age) <= 120:
            return int(age)
        print("Age must be a number between 1 and 120")


# clears the terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# prints a text file
def show_text_file(filename):
    try:
        with open(os.path.join(BASE, filename), "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Could not find {filename}!")


# saves the game
def save_game(player, tower_rooms):
    item_names = []
    for item in player.items:
        item_names.append(item.name)

    taken = [room.name for room in tower_rooms if room.item is None]

    save_data = {
        "name": player.name,
        "age": player.age,
        "room": player.location.name,
        "score": player.score,
        "items": item_names,
        "solved": sorted(player.solved),
        "recycled": player.recycled,
        "taken": taken
    }

    with open(SAVE_PATH, "w") as file:
        json.dump(save_data, file)


# makes a player from save data
def build_player(save_data, rooms, tower_rooms):
    room = rooms[0]
    for saved_room in rooms + tower_rooms:
        if saved_room.name == save_data["room"]:
            room = saved_room

    player = Player(save_data["name"], room, save_data.get("age", 0))
    player.score = save_data["score"]
    player.solved = set(save_data["solved"])
    player.recycled = save_data.get("recycled", 0)

    for tower_room in tower_rooms:
        if tower_room.name in save_data.get("taken", []):
            tower_room.item = None

    for item_name in save_data["items"]:
        for item in SHOP_POTIONS + SCRAPS:
            if item.name == item_name:
                player.items.append(item)

    return player


# loads the game
def load_game(rooms, tower_rooms):
    try:
        with open(SAVE_PATH, "r") as file:
            save_data = json.load(file)
        player = build_player(save_data, rooms, tower_rooms)
    except (FileNotFoundError, ValueError, KeyError, TypeError):
        return None

    return player


# main menu
def main():
    rooms = [Room("Riddle 1"), Room("Riddle 2"), Room("Riddle 3")]
    tower_rooms = build_tower_rooms()

    show_text_file("intro.txt")
    show_text_file("instructions.txt")

    player = load_game(rooms, tower_rooms)
    if player is not None:
        continue_input = input(f"Continue as {player.name}? enter 1 to continue, 2 to start a new game. ")
        if continue_input != "1":
            player = None

    if player is None:
        tower_rooms = build_tower_rooms()
        name = ask_name()
        age = ask_age()
        player = Player(name, rooms[0], age)
        print(f"Greetings {name}, age {age}. Welcome to Codebreaker! ")
    else:
        print(f"Greetings {player.name}, Welcome back to Codebreaker! ")

    # menu loop
    while True:
        input("\nPress enter to continue ")
        clear_screen()
        print("1. Play!")
        print("2. Progress!")
        print("3. Quit Game!")
        print("4. Shop!")
        print("5. Inventory!")
        print("6. Open the tower door!")
        print("7. Recycle!")
        print("8. Explore the tower!")
        command = input("Choose option 1-8! ")

        if command == "3":
            save_game(player, tower_rooms)
            print("Game saved.")
            print("Hope to see you soon!")
            break
        elif command == "1":
            play_riddle(player, rooms)
        elif command == "2":
            show_progress(player)
        elif command == "4":
            shop(player)
        elif command == "5":
            inventory(player)
        elif command == "6":
            if open_door(player):
                if os.path.exists(SAVE_PATH):
                    os.remove(SAVE_PATH)
                break
        elif command == "7":
            recycle(player)
        elif command == "8":
            explore(player, tower_rooms)
        elif command not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print(f"{command} is not a real option!")


if __name__ == "__main__":
    main()
