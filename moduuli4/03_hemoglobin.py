# ============================================
# Module 4, Exercise 3: Hemoglobin checker
# ============================================
# Goal: ask for biological gender + hemoglobin value (g/l),
#       tell the user if it's low, normal, or high.
#
# The normal ranges:
#   Female: 117-155 g/l
#   Male:   134-167 g/l
#
# Steps:
# 1. Ask the user to enter their biological gender (e.g. "female" or "male")
#    Store it in a variable.
# 2. Ask the user to enter their hemoglobin value.
#    Store it in a variable (remember: this needs to be a number, not text!)
# 3. If gender is "female":
#      - if value is below 117: print "low"
#      - elif value is above 155: print "high"
#      - else: print "normal"
# 4. Elif gender is "male":
#      - if value is below 134: print "low"
#      - elif value is above 167: print "high"
#      - else: print "normal"
# 5. Else (gender wasn't recognized): print an error message.
#
# Tip: this is basically the same shape as fish.py and 2.py (if/elif/else),
# just with an extra layer because there are two different ranges.
# 16:34 10.09.26
gender = input("What is your gender? female/male ")
hemoglobin = input("What is your hemoglobin value? ")
gendervalue = gender
hemovalue = int(hemoglobin)
if gender == "female" and hemovalue < 117:
    print("Low")
elif gender == "female" and hemovalue > 155:
    print("High")
elif gender == "male" and hemovalue < 134:
    print("Low")
elif gender == "male" and hemovalue > 167:
    print("High")
elif gender == "female" and hemovalue >= 117 and hemovalue <= 155:
    print("Normal")
elif gender == "male" and hemovalue >= 134 and hemovalue <= 167:
    print("Normal")
else:
    print("Error: Gender wasn't recognized ")


