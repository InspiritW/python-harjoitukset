# ============================================
# Module 6, Exercise 1: Roll multiple dice
# ============================================
# Goal: ask how many dice to roll, roll them all once, print the sum.
# You MUST use a for loop here (this whole module is about for loops).
#
# Steps:
# 1. Import random.
# 2. Ask the user how many dice to roll. Convert to int.
# 3. Make a variable to hold the total, e.g. total = 0
# 4. Use a for loop that repeats that many times:
#      for i in range(number_of_dice):
#    Inside it: roll one die (random.randint(1, 6)) and add it to total.
# 5. After the loop: print the total.
#11:06 14.09.2026   
import random
howmany = int(input("How many dice to roll? "))
total = 0
for i in range(howmany):
    roll_dice = (random.randint(1, 6))
    total += roll_dice
print(total)
