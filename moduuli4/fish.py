#Ask for input: Prompt the fisher to type in the length of the zander (in centimeters).
#Set the rule: The minimum size limit is 42 cm
#Condition A (If the fish is too small — less than 42 cm):
#Tell them to throw the fish back into the lake.
#Math step: Subtract the fish's length from 42.
#Tell them exactly how many centimeters too short it was.
#Condition B (If the fish is big enough — 42 cm or more):
#Let them know they can keep it.

lenzan = int(input("Lenght of zander in cm "))
length = 42
if lenzan < length:
    print("Throw the fix into the lake")
    minus = length - lenzan
    print(f"your fish is {minus} cm too short!")
else:
    print("You can keep it")
    