# ============================================
# Module 8, Exercise 3: Airport database (dictionary)
# ============================================
# Goal: a little menu program that stores airport ICAO codes -> names in
# a DICTIONARY, and lets the user add new airports or look one up.
#
# Steps:
# 1. Make an empty dictionary: airports = {}
# 2. Start a while loop (while True:) — this is your menu loop.
# 3. Print the menu options and ask what the user wants to do, e.g.
#    "1. Add airport   2. Find airport   3. Quit"
# 4. If they choose "add":
#      - ask for the ICAO code (e.g. "EFHK")
#      - ask for the airport name
#      - store it: airports[code] = name
# 5. If they choose "find":
#      - ask for an ICAO code
#      - look it up and print the name: print(airports[code])
#      - (bonus/careful: what happens if the code isn't in the
#        dictionary? Look up dict.get() to handle that safely)
# 6. If they choose "quit": break out of the loop.
# 7. Loop keeps repeating (back to step 3) until the user quits.
