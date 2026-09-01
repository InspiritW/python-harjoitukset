# ============================================
# Module 5, Exercise 4: Guess the number game
# ============================================
# Goal: computer picks a random number 1-10, player keeps guessing until right.
#
# Steps:
# 1. Import the random module (see concepts/04_random_module.py if you need
#    a refresher on how that works).
# 2. Pick ONE random number between 1 and 10 and store it in a variable
#    BEFORE the loop starts. (If you pick a new number inside the loop,
#    the target keeps changing — that's a bug, not the game!)
# 3. Start a while loop that keeps running until the guess is correct.
# 4. Inside the loop: ask the user to guess a number.
# 5. Compare the guess to the secret number:
#      - guess too high -> print "Too high"
#      - guess too low  -> print "Too low"
#      - guess correct  -> print "Correct" and end the loop
