# 18:15 valmis, 01.09.2026

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
    score = 0
    riddle_1 = 0
    while True:
        print("1. Play!")
        print("2. Progress!")
        print("3. Quit Game!")
        command = input("Choose option 1-3! ")
        if command == "3":
            print("Hope to see you soon!")
            break
        elif command == "1":
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
        elif command == "2":
            print("Here you can see which riddles you have completed. ")
            if riddle_1 == 1:
                print("Riddle 1 is completed!")
            elif riddle_1 == 0:
                print("Riddle 1 is not completed!")
        elif command not in ("1", "2", "3"):
            print(f"{command} is not a real option!")
        