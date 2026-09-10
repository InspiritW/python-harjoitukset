# 18:15 valmis, 01.09.2026
# 3. 18:24 valmis, 10.09.2026

ask_name = input("What is your name? ")
ask_age = input("What is your age? ")
name = ask_name
age = ask_age
print(f"{name}, {age}")
age_int = int(age)
if age_int < 12:
    print("You are underage!")
else:
    print(f"Greetings {name}, Welcome to Codebreaker! ")
    potions = []
    score = 0
    riddle_1 = 0
    shop_potions = [
        {"Name": "Hint Potion", "cost": 1, "Info": "Gives you an extra hint!"},
        {"Name": "Answer Potion", "cost": 3, "Info": "Gives you the answer!"}
    ]
    def show_progress():
        print("Here you can see which riddles you have completed. ")
        if riddle_1 == 1:
           print("Riddle 1 is completed!")
        elif riddle_1 == 0:
           print("Riddle 1 is not completed!")
    def play_riddle_1():
                global riddle_1
                global score
                print("Riddle 1!")
                print("Digit 1: I am one.")
                print("Digit 2: I am seven more than digit 1.")
                print("Digit 3: I am two less than digit 2.")
                print("Digit 4: I am one less than digit 3.")
                answer_1 = str(1865)
                while True:
                    user_answer = input("What am i? ")
                    if user_answer != answer_1:
                        print("Wrong answer, try again!")
                        print("Hint, The year a major war ended")
                    elif user_answer == answer_1:
                        print("Great job!")
                        riddle_1 += 1
                        score += 1
                        break
                next_step = input("Return to menu? enter 1. \nGo to the next riddle? Enter 2!\nSelect 1 or 2! >")
                if next_step == "2":
                    print("More riddles coming soon!")
                    pass
                elif next_step == "1":
                    pass
    def quit_game():
        print("Hope to see you soon!")
    def shop():
        leave_shop = False
        global score
        print("Welcome to the shop!")
        print("You can buy potions here that help you in many ways!")

        for potion in potions:
            if score <= 1:
                print(f"You have {score} coin")
            else:
                print(f"You have {score} coins")
        for potion_item in shop_potions:
            if potion_item['cost'] <= 1:
                print(f"Potion: {potion_item['Name']}, costs {potion_item['cost']} coin, {potion_item['Info']}")
            else:
                print(f"Potion: {potion_item['Name']}, costs {potion_item['cost']} coins, {potion_item['Info']}")
        
        while True:
            which_potion = input("Which potion do you want to buy? ")
            potion_selected = which_potion
            for potion_item in shop_potions:
                if potion_item['Name'] == which_potion:
                    if score >= potion_item['cost']:
                        choise_input = input("You can afford this, do you want to buy it? 1 for yes, 2 for no. ")
                        choise = int(choise_input)
                        if choise == 1:
                            print("Thank you for shoppin!")
                            potions.append(potion_item['Name'])
                            score -= potion_item['cost']
                            leave_shop = True
                            break
                        elif choise == 2:
                            print("Alright.")
                            break
                        elif choise not in (1, 2):
                            print("Non-existant potion selected. Try again.")
                    else:
                        print("You cannot afford this.")
                        break
            if leave_shop == True:
                break
    def inventory():
        print("Welcome to your inventory!")
        print("Here you can view your available potions!")
        for potion in potions:
            print(f"You have  {potion}")
        
    while True:
        print("1. Play!")
        print("2. Progress!")
        print("3. Quit Game!")
        print("4. Shop!")
        print("5. Inventory!")
        command = input("Choose option 1-5! ")
        if command == "3":
            quit_game()
            break
        elif command == "1":
             play_riddle_1()
        elif command == "2":
            show_progress()
        elif command == "4":
            shop()
        elif command == "5":
            inventory()
        elif command not in ("1", "2", "3", "4", "5"):
            print(f"{command} is not a real option!")
        