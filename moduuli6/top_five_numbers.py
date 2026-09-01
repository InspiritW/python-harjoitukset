# ============================================
# Module 6, Exercise 2: Top 5 numbers
# ============================================
# Goal: ask for numbers until an empty string is entered, then print the
# five biggest numbers, sorted from biggest to smallest.
#
# Steps:
# 1. Make an empty list, e.g. numbers = []
# 2. Loop asking for input (while True: ... break on empty string,
#    same pattern as moduuli5/min_max_numbers.py). Convert each entry
#    to a number and add it to the list with numbers.append(...)
# 3. After the loop, sort the list with the reverse=True trick:
#      numbers.sort(reverse=True)
#    This sorts biggest-to-smallest, in place.
# 4. Use a for loop (for n in numbers[:5]:) to print the first five
#    entries, one per line.
#    (numbers[:5] means "just the first 5 items of the list" — look up
#    "python list slicing" if that's new to you.)
