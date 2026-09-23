# ============================================
# Module 5, Exercise 3: Smallest and largest number
# ============================================
# Goal: keep asking for numbers until the user enters an empty string ("").
# Then print the smallest and the largest number that was entered.
#
# Steps:
# 1. Before the loop, you need somewhere to remember the numbers you've seen.
#    Two options:
#      a) keep a list and append every number to it, OR
#      b) keep two variables `smallest` and `largest` and update them as you go
#    (Pick whichever makes more sense to you — (a) is easier to reason about,
#    (b) is more efficient. Either is fine.)
# 2. Start a while loop (while True:)
# 3. Ask the user to enter a number as text (input()).
# 4. If the text is empty (""): break out of the loop.
# 5. Otherwise: convert it to a number (int() or float()) and update your
#    list / smallest / largest.
# 6. After the loop ends, print the smallest and largest values found.
#
# Watch out: what happens on the very FIRST number, when you don't have
# a "smallest so far" yet? Think about how you'd handle that.
#12:08 11.09.2026
numbers_seen = []
while True:
    ask = input("Enter number")
    if ask == "":
        break
    else:
        convert = int(ask)
        numbers_seen.append(convert)
if numbers_seen:
    smallest = min(numbers_seen)
    largest = max(numbers_seen)
    print(f"Smallest: {smallest}, Largest: {largest}")
else:
    print("No numbers were entered.")
