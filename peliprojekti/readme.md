# Codebreaker

Jonatan Buskila

## Structure

The game is split into modules. Every module can also be run on its own for testing.

- `item.py` — `Item` and `Potion`: a potion is an item
- `room.py` — `Room`: the three riddle chambers
- `player.py` — `Player`: name, location, items, score and solved riddles
- `peli.py` — the main program: the menu, the riddles, the shop and saving
- `intro.txt` / `instructions.txt` — the texts shown when the game starts
- `savegame.json` — the saved game (created when you quit)

`play_riddle` in `peli.py` finds the next unsolved riddle and moves the player there automatically.