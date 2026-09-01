# ============================================
# Concept: if / elif / else
# ============================================
# Your program needs to make decisions. if/elif/else lets it run
# different code depending on a condition.
#
# Rules:
# - Python checks conditions TOP TO BOTTOM and stops at the first True one.
# - elif = "else if" — only checked if everything above it was False.
# - else = the catch-all, runs if nothing above matched.
# - You can have zero or many elifs, and else is optional.

# --- Example (run this file as-is) ---
temperature = int(input("What's the temperature (C)? "))

if temperature < 0:
    print("Freezing!")
elif temperature < 15:
    print("Cold")
elif temperature < 25:
    print("Nice")
else:
    print("Hot")

# Common comparison operators: == (equal), != (not equal),
# <, >, <=, >=
# Note: == checks equality. A single = ASSIGNS a value — mixing these
# up is one of the most common beginner bugs.

# You can also combine conditions:
#   if age >= 18 and has_id:
#   if day == "saturday" or day == "sunday"

# --- Your turn ---
# What would you add here to also handle temperature == 0 as a special
# case ("Exactly freezing") — where would that elif need to go, and why
# does the ORDER of your conditions matter?
