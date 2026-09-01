# ============================================
# Module 8, Exercise 1: What season is it?
# ============================================
# Goal: ask for a month number (1-12), print the season.
# Winter starts with December. Each season = 3 months.
# Store the season names in a TUPLE (not a list — tuples don't change,
# which fits here since the seasons never change).
#
# Steps:
# 1. Make a tuple of the 4 season names in month order starting from
#    December, e.g.:
#      seasons = ("winter", "winter", "winter", "spring", "spring", "spring",
#                 "summer", "summer", "summer", "autumn", "autumn", "autumn")
#    (Think about why starting the list from December, not January, makes
#    the indexing easier here.)
# 2. Ask for a month number (1-12), convert to int.
# 3. Figure out the right index into `seasons` from the month number.
#    Hint: December (12) should map to index 0. Try month % 12 and think
#    through a couple examples by hand (month 1 -> ?, month 12 -> ?).
# 4. Print seasons[that index].
