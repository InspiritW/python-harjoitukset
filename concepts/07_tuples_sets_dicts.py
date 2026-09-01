# ============================================
# Concept: tuple vs set vs dict (vs list, for comparison)
# ============================================
# You already know lists: ordered, can have duplicates, CAN be changed.
#
# TUPLE  — ordered, can have duplicates, CANNOT be changed after creation.
#          Use when the data shouldn't change (e.g. the 4 seasons).
seasons = ("winter", "spring", "summer", "autumn")
print(seasons[1])          # "spring" — access by position, just like a list
# seasons[1] = "x"          # this would ERROR — tuples are locked

# SET    — unordered, NO duplicates allowed, CAN be changed.
#          Use when you just need to track "have I seen this before?"
seen_names = set()
seen_names.add("Alice")
seen_names.add("Alice")    # adding the same thing twice does nothing
print(seen_names)          # {"Alice"} — only appears once
print("Alice" in seen_names)   # True — fast way to check membership

# DICT (dictionary) — key/value PAIRS. Instead of looking things up by
#          position (like a list), you look them up by a key you choose.
airports = {}
airports["EFHK"] = "Helsinki-Vantaa"
airports["EFTP"] = "Tampere-Pirkkala"
print(airports["EFHK"])        # "Helsinki-Vantaa"
print(airports.get("EFXX"))    # None (safe — doesn't crash like [] would)

# --- Your turn ---
# What would you add here to loop through the `airports` dictionary and
# print every code and name? (Hint: look up `.items()` on a dictionary.)
