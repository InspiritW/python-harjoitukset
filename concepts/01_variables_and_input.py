# ============================================
# Concept: Variables + input() + type conversion
# ============================================
# A variable is just a labeled box that holds a value.
#
# input() ALWAYS gives you back text (a string), even if the user types
# a number. If you want to do math with it, you have to convert it.

# --- Example (run this file as-is) ---
name = input("What's your name? ")   # this is text (a string)
print(f"Hello, {name}!")

age_text = input("What's your age? ")     # still text, even though it's digits
age_number = int(age_text)                # now it's a real integer
print(f"Next year you'll be {age_number + 1}")

# int()   -> converts to a whole number
# float() -> converts to a decimal number
# str()   -> converts a number back to text (useful for some f-strings,
#            though f-strings usually handle this for you automatically)

# f-strings: put an f right before the quote, and {variable} inside the
# string gets replaced with the variable's value. That's it.

# --- Your turn ---
# Try this yourself below (or in a scratch file):
# What happens if you try int("hello")? Run it and read the error message
# carefully — errors in Python usually tell you exactly what went wrong.
# What would you add here to ask for a decimal number (like a price) and
# print it back doubled?
