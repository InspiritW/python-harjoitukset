# ============================================
# Module 7, Exercise 2: Dice with any number of sides
# ============================================
# Goal: same as before, but now the function takes a parameter for how
# many sides the dice has. The game now rolls until it hits the MAXIMUM
# value on that dice (which the user chooses).
#
# Steps:
# 1. Define: def roll_dice(sides):
#    Inside: return a random number between 1 and `sides`.
# 2. In the main program: ask the user for the max number on the dice
#    (e.g. 21 for a 21-sided dice). Convert to int.
# 3. Loop, calling roll_dice(sides_the_user_gave) each time, printing
#    each roll, until the result equals that max number.
