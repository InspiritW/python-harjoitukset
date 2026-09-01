# ============================================
# Module 7, Exercise 6: Which pizza is the better deal?
# ============================================
# Goal: a function that calculates price per square meter for a round
# pizza. Main program compares two pizzas and says which is better value.
#
# Steps:
# 1. Define a function that takes diameter (cm) and price (euros):
#      def unit_price(diameter_cm, price):
#    Inside:
#      - radius = diameter_cm / 2, then convert to meters (divide by 100)
#      - area = pi * radius^2   (use 3.14159, or `import math` and math.pi)
#      - return price / area
# 2. In the main program: ask for diameter + price of pizza 1, then
#    diameter + price of pizza 2.
# 3. Call unit_price() for each pizza — this is the whole point, you must
#    use the function, not repeat the formula twice.
# 4. Compare the two results and print which pizza has the LOWER unit
#    price (that's the better deal).
