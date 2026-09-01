# ============================================
# Concept: reading and writing files
# ============================================
# So far your programs forget everything when they close. Reading and
# writing files lets you save data between runs.
#
# The safe way to open a file is with `with` — it automatically closes
# the file for you, even if something goes wrong.

# --- Example (create a file called example.txt with some text in it
#     next to this file first, then run this) ---

# READING a whole file:
# with open("example.txt", "r") as f:     # "r" = read mode
#     content = f.read()
# print(content)

# READING line by line:
# with open("example.txt", "r") as f:
#     for line in f:
#         print(line.strip())    # .strip() removes the trailing newline

# WRITING to a file (this OVERWRITES the whole file):
# with open("output.txt", "w") as f:      # "w" = write mode
#     f.write("Hello, file!\n")

# APPENDING (adds to the end instead of overwriting):
# with open("output.txt", "a") as f:      # "a" = append mode
#     f.write("Another line\n")

# For SAVING GAME STATE, a common trick: write each piece of data as
# its own line, then read it back the same way, in the same order.
#   with open("save.txt", "w") as f:
#       f.write(f"{player_name}\n")
#       f.write(f"{player_score}\n")

# --- Your turn ---
# What would you add here to write a small save file with your game's
# player name and current room, then read it back and print it, to
# prove it round-trips correctly?
