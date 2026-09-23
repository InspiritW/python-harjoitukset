# ============================================
# Module 4, Exercise 4: Leap year checker
# ============================================
# Goal: ask the user for a year, tell them if it's a leap year.
#
# The rule (read carefully, it has an exception inside an exception):
#   - If the year is divisible by 4        -> leap year...
#   - ...UNLESS it's also divisible by 100 -> then it's NOT a leap year...
#   - ...UNLESS it's ALSO divisible by 400 -> then it IS a leap year after all.
#
# Examples: 2024 -> leap year (divisible by 4, not by 100)
#           1900 -> NOT a leap year (divisible by 100, not by 400)
#           2000 -> leap year (divisible by 400)
#
# Steps:
# 1. Ask the user to enter a year. Store it as an integer.
# 2. Use the % (modulo) operator to check divisibility.
#    Reminder: year % 4 == 0  means "year is evenly divisible by 4"
# 3. Write the condition. One way to think about it:
#      if year is divisible by 400: leap year
#      elif year is divisible by 100: NOT a leap year
#      elif year is divisible by 4: leap year
#      else: not a leap year
#    (Notice the order matters here! Try to think through why.)
# 4. Print a clear message either way, e.g. "2024 is a leap year."
#    or "1900 is not a leap year."
enter_year = input("Enter a year. ")
year_entered = int(enter_year)
def leap_year():
        if year_entered % 400 == 0:
            print("Leap year!")
        elif year_entered % 100 == 0:
            print("Not a leap year!")
        elif year_entered % 4 == 0:
            print("Leap year!")
        else:
            print("Not a leap year!")
leap_year()