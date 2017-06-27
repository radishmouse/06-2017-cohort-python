
# Just generating the sequence of letters/numbers
seq = []
jumble = "123abcdabcd123xyz987"
for l in jumble:
  seq.append(l)

# Create a variable for a new sequence
new_seq = []
# Iterate through our sequence
for i in seq:
  # If the current letter is not in the sequence,
  # add it.
  if i not in new_seq:
    new_seq.append(i)
print new_seq