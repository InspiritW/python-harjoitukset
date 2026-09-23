# ============================================
# Module 5, Exercise 6: Estimating pi with random points
# ============================================
# Goal: use random points to approximate the value of pi (Monte Carlo method).
#
# The idea: scatter random points in a 2x2 square (from -1 to 1 on both axes).
# A point is "inside the circle" if x^2 + y^2 < 1.
# The fraction of points inside the circle vs total points, times 4,
# approximates pi.  pi ≈ 4 * (points inside circle) / (total points)
#
# Steps:
# 1. Import random.
# 2. Ask the user how many random points to generate (N). Convert to int.
# 3. Make a counter for points inside the circle, e.g. n = 0
# 4. Use a while (or for) loop that runs N times:
#      a. generate a random x between -1 and 1  -> random.uniform(-1, 1)
#      b. generate a random y between -1 and 1
#      c. check if x**2 + y**2 < 1
#      d. if yes, add 1 to your "inside the circle" counter
# 5. After the loop: calculate pi_estimate = 4 * n / N
# 6. Print the estimate. Try it with a small N (like 100) and a big N
#    (like 1,000,000) and see how the accuracy changes.
#12:53 11.09.2026
import random
how_many = int(input("how many points to generate (N)"))
n = 0
generated = 0
while True:
    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1)
    if random_x ** 2 + random_y ** 2 < 1:
        n += 1
    generated += 1
    if generated >= how_many:
        break

pi_estimate = 4 * n / how_many
print(pi_estimate)
