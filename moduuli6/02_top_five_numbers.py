# ============================================
# Module 6, Exercise 2: Top 5 numbers
# ============================================
# Goal: ask for numbers until an empty string is entered, then print the
# five biggest numbers, sorted from biggest to smallest.
#14.09.2026 12:34

numbers = []
while True:
    ask = input("Enter numbers")
    if ask == "":
        break
    convert = int(ask)
    numbers.append(ask)
numbers.sort(reverse=True)
for number in numbers[:5]:
    print(number)