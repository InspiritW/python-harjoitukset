# ============================================
# Module 8, Exercise 2: New name or existing name?
# ============================================
# Goal: keep asking for names until an empty string is entered. After each
# name, say whether it's new or one you've already seen. At the end, list
# all the names. Use a SET (not a list) to store them.
#
# A set automatically ignores duplicates and doesn't keep order — that's
# exactly what we want here. See 00_concept_tuples_sets_dicts.py, above.
#
# Steps:
# 1. Make an empty set
# 2. Start a while loop (while True:)
# 3. Ask for a name. If it's empty (""): break.
# 4. Check: if the name is already in the set (use the `in` keyword) ->
#    print "Existing name". Otherwise -> print "New name" and add it to
#    the set with names.add(name).
# 5. After the loop: use a for loop to print every name in the set,
#    one per line.
