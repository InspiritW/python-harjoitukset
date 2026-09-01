# ============================================
# Module 5, Exercise 5: Login with limited attempts
# ============================================
# Goal: ask for username + password, allow up to 5 tries.
#
# Correct username: python
# Correct password: rules
#
# Steps:
# 1. Make a counter variable for how many attempts have been used, e.g.
#    attempts = 0
# 2. Start a while loop that runs while attempts < 5
# 3. Inside the loop: ask for username, ask for password.
# 4. Add 1 to your attempts counter.
# 5. If username == "python" and password == "rules":
#      print "Welcome" and break out of the loop.
#    Else: (loop continues automatically, asks again)
# 6. After the loop: if the login was never correct after 5 tries,
#    print "Access denied".
#    Hint: you'll need a way to know WHY the loop ended (ran out of
#    attempts vs. got it right) — a boolean flag variable can help here,
#    e.g. logged_in = False, set to True when the login succeeds.
