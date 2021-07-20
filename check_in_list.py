acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
word = input("Type the acronym you are searching:")
word1 = word.upper()

if word1 in acronyms:
    print(word + " is in the list")
else:
    print(word + " is NOT in the list")