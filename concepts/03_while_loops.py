# ============================================
# Concept: while loops
# ============================================
# A `while` loop repeats AS LONG AS a condition stays True. Use it when
# you don't know in advance exactly how many times you'll repeat
# (unlike a `for` loop over a fixed range).
#
# THE #1 WHILE-LOOP BUG: forgetting to update the thing the condition
# checks. If nothing inside the loop ever makes the condition False,
# it runs forever (an "infinite loop" — if that happens, Ctrl+C stops it).

# --- Example (run this file as-is) ---
count = 1
while count <= 5:
    print(f"count is {count}")
    count = count + 1   # <-- without this line, this loop never ends!
print("done")

# A very common pattern: "loop forever, break when a condition is met"
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break   # break immediately exits the loop, skipping the rest
    print(f"You typed: {answer}")

# --- Nested loops (a loop inside another loop) ---
# The inner loop runs ALL THE WAY THROUGH for every single pass of the
# outer loop. Useful for grids, tables, "for each X, do every Y".
for row in range(3):
    for col in range(2):
        print(f"row {row}, col {col}")
# Output order: (0,0) (0,1) (1,0) (1,1) (2,0) (2,1)
# — the inner loop finishes completely before the outer loop moves on.

# --- while/else ---
# The `else` on a while loop runs only if the loop finished NORMALLY
# (condition became False) — it's SKIPPED if the loop was stopped early
# with `break`. Rarely used, but you'll see it in the course material,
# so it's worth recognizing:
n = 1
while n <= 3:
    print(n)
    n += 1
else:
    print("loop finished without a break")

# --- Your turn ---
# What would you add here to count DOWN from 5 to 1 instead of up?
# What's the smallest change you'd need to make to the example above?
#
# Also: rewrite the nested loop example so the inner loop breaks out
# early once row == col — what happens to the rest of that inner pass?
