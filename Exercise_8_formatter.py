formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "hmm", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, "hmm", formatter, formatter))
print(formatter.format(
    "Let us go then",
    "You and I",
    "When the evening is spread out against the sky",
    "Like a patient etherized on a table"
))