# Ask the user to enter a cabin class (LUX, A, B, or C)
# Store their answer in a variable

# If cabin_class is "LUX": print "Upper-deck cabin with a balcony"
# Elif cabin_class is "A": print "Above the car deck, equipped with a window"
# Elif cabin_class is "B": print "Windowless cabin above the car deck"
# Elif cabin_class is "C": print "Windowless cabin below the car deck"
# Else: print "Unknown cabin class"

cabin_class = input("Enter a cabin class ").upper()
if cabin_class not in ["LUX", "A", "B", "C"]:
    print("LUX,A,B,C")
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window")
elif cabin_class == "B":
    print("Windowless cabin above the car deck")
elif cabin_class == "C":
    print("Windowless cabin below the car deck")
else:
    print("Unknown cabin class")