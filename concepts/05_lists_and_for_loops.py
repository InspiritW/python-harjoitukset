# ============================================
# Concept: lists + for loops
# ============================================
# A list holds multiple values in order, in one variable.
# A `for` loop is for when you want to do something a KNOWN number of
# times, or once for every item already in a list.

# --- Example (run this file as-is) ---
fruits = ["apple", "banana", "cherry"]

# for/in loop: goes through each existing item
for fruit in fruits:
    print(f"I like {fruit}")

# for loop with range(): repeats a fixed number of times
for i in range(3):          # 0, 1, 2  (range stops BEFORE the number given)
    print(f"i is now {i}")

# building a list as you go:
squares = []
for n in range(1, 6):       # 1, 2, 3, 4, 5
    squares.append(n * n)
print(squares)              # [1, 4, 9, 16, 25]

# useful list things:
fruits.append("date")       # add to the end
print(len(fruits))          # how many items
fruits.sort()                # sorts in place (alphabetical or numeric)
fruits.sort(reverse=True)    # sorts backwards

# --- Your turn ---
# What would you add here to print each fruit TOGETHER WITH its
# position in the list (1. apple, 2. banana, ...)? Look up the
# built-in enumerate() function — that's the tool for this.
