# ============================================
# Module 6, Exercise 3: Is it a prime number?
# ============================================
# Goal: ask for an integer, say whether it's prime.
# A prime number can only be evenly divided by 1 and itself.
#
# Steps:
# 1. Ask the user for an integer.
# 2. Make a variable is_prime = True (assume it's prime until proven otherwise)
# 3. Use a for loop to test every possible divisor from 2 up to (number - 1):
#      for i in range(2, number):
# 4. Inside the loop: if number % i == 0, that means it DID divide evenly,
#    so it's not prime -> set is_prime = False
#    (you can also `break` here immediately, no point checking more)
# 5. After the loop: if is_prime is True, print "prime". Else print "not prime".
#
# Watch out: what should happen for numbers less than 2? (0, 1, negative
# numbers aren't prime by definition.) Think about where to handle that.

number = int(input("Enter an integer! "))
is_prime = True
if number <= 0 or number == 1:
    is_prime = False
for i in range(2, number):
    if number % 1 == 0:
        is_prime = False
        break
    elif number <= 0:
        is_prime = False
        break
if is_prime == True:
    print("Prime")
else:
    print("Not prime")
