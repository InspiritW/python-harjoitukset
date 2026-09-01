# ============================================
# Concept: functions
# ============================================
# A function is a named, reusable block of code. You DEFINE it once,
# then CALL it as many times as you want.
#
# - Parameters = the inputs the function expects (in the parentheses)
# - return = hands a value back to whoever called the function.
#   This is DIFFERENT from print()! print() just displays something
#   on screen — it doesn't give the value back to your code.
#   A function with no `return` gives back None.

# --- Example (run this file as-is) ---
def add(a, b):
    result = a + b
    return result

total = add(3, 4)     # total is now 7 — we can use it in more code
print(total)
print(add(10, 20))    # you can also use the return value directly

def greet(name):
    print(f"Hello, {name}!")   # this one prints but returns nothing

greet("Jonatan")

# A function's parameters and any variables it creates only exist
# INSIDE that function ("local scope") — they disappear once it's done.

# --- Your turn ---
# What would you add here to write a function `is_even(number)` that
# RETURNS True or False depending on whether the number is even?
# (Don't print inside it — return the boolean, then print the result
# where you call it.)
