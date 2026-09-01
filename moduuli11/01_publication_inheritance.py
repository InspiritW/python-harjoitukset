# ============================================
# Module 11, Exercise 1: Publication -> Book / Magazine
# ============================================
# Goal: a Book and a Magazine are both kinds of Publication. They share
# a `name`, but each has its own extra property.
# See 00_concept_inheritance.py, above, first if this is new.
#
# Steps:
# 1. Define a base class Publication with __init__(self, name) storing
#    self.name = name.
# 2. Define class Book(Publication) — this means "Book IS A Publication".
#    Its __init__(self, name, author, pages) should:
#      - call the parent's initializer first: super().__init__(name)
#      - then store self.author = author, self.pages = pages
# 3. Define class Magazine(Publication) the same way, but with a
#    chief_editor property instead of author/pages.
# 4. Add a print_information(self) method to BOTH Book and Magazine
#    (each one prints its own name plus its own extra info).
# 5. In the main program: create a Magazine("Aku Ankka", "Aki Hyyppä")
#    (Donald Duck comic in Finland) and a
#    Book("Compartment No. 6", "Rosa Liksom", 192).
# 6. Call print_information() on both and check the output looks right.
