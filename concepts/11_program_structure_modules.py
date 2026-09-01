# ============================================
# Concept: organizing code into modules/files
# ============================================
# Once a project grows (like your game project), one giant file gets
# hard to navigate. Python lets you split code across multiple .py
# files ("modules") and import what you need.

# --- Example: imagine two files in the same folder ---
#
# player.py:
#   class Player:
#       def __init__(self, name):
#           self.name = name
#
# main.py:
#   from player import Player   # import the Player class from player.py
#
#   p = Player("Jonatan")
#   print(p.name)
#
# You can also group related files into a folder ("package") — put an
# empty file called __init__.py inside that folder, and Python treats
# the whole folder as importable.
#
# For the game project, a sensible structure might be:
#   project/
#     main.py       <- the menu loop, starts the game
#     player.py      <- Player class
#     room.py        <- Room class
#     item.py        <- Item class

# --- Your turn ---
# Look at your own project/ folder right now. What would you split into
# separate files, and why would that make it easier to find things
# later? Write your plan down in project/readme.md.
