# ============================================
# Concept: the random module
# ============================================
# Python doesn't have "random" built in by default — you have to ask
# for it explicitly with `import random` at the very top of your file.

import random

# --- Example (run this file as-is) ---
dice_roll = random.randint(1, 6)       # a random WHOLE number, 1 to 6 (both included)
print(f"You rolled a {dice_roll}")

coin_flip = random.choice(["heads", "tails"])   # random pick from a list
print(f"Coin landed on: {coin_flip}")

decimal_value = random.uniform(-1, 1)  # a random DECIMAL number between -1 and 1
print(f"Random decimal: {decimal_value}")

# random.randint(a, b)  -> whole number, a and b both possible
# random.uniform(a, b)  -> decimal number between a and b
# random.choice(a_list) -> picks one random item from a list

# --- Your turn ---
# What would you add here to simulate rolling TWO dice and printing
# their sum? (Hint: you already know how to call randint() twice.)
