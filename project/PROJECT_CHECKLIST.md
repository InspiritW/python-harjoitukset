# Game project — checkpoint overview

Your game is ONE ongoing program (`project/main.py` + whatever other
files you split it into later) that grows at each course checkpoint.
This file lists what's expected at each checkpoint, in order. Don't try
to do future checkpoints early — build it up as the course gets there.

## Checkpoint 1 (after module 3) — done via project/main.py
- [ ] `project/readme.md` has your game's name as a heading + your name
- [ ] Program asks for player name + age, stores them, prints them

## Checkpoint 2 (after module 5) — "Main Menu"
- [ ] If the entered age is under 12: print that they're a minor, and
      shut the program down (don't show the menu at all).
- [ ] Otherwise: greet the player, then show a main menu, and keep
      asking for commands in a loop until the player types "lopeta".
      (This needs a `while True:` loop around your menu, with a
      `break` when the command equals "lopeta" — see
      moduuli5/00_concept_while_loops.py.)
- [ ] Add a few made-up commands (whatever fits your game) that each
      print something different. After running a command, show the
      menu again (the loop just goes around again naturally).

## Checkpoint 3 (after module 7) — "Menu functions + inventory"
- [ ] Turn at least 3 of your menu commands into their own FUNCTIONS,
      called from inside the menu loop (see moduuli7/00_concept_functions.py).
- [ ] One function must ask the player for something (like an item
      name) and add it to a list variable.
- [ ] Another function must print out everything currently in that list.
- [ ] The rest of the functions can do whatever fits your game.

## Checkpoint 4 (after module 12) — "Organize + introduce objects"
- [ ] Split your code into separate files/modules as it makes sense
      (see moduuli12/00_concept_program_structure_modules.py). Update
      project/readme.md describing how you organized it.
- [ ] Create three classes: Player, Room, Item.
      - Item: has at least a name and a weight.
      - Player: has at least a name, a list of items they're carrying,
        and their current location (a Room).
      - Room: has at least a name, and possibly one Item in it.
- [ ] When the program starts: create one Player object, and a few
      Room and Item objects.
- [ ] Add player actions for moving between rooms and collecting an
      item from a room — wire these into your menu.

## Checkpoint 5 (after module 13) — "File handling"
- [ ] Create `intro.txt` and `instructions.txt` next to main.py. Move
      your game's intro text / instructions into those files, and READ
      them from your program instead of hardcoding the text
      (see moduuli13/00_concept_file_handling.py).
- [ ] Save the game's state to a file (player name, location, items,
      etc. — whatever your game needs to resume) so the player can
      close the program and pick up later, e.g. by entering their name
      or a saved code when the program starts.
