
original = "here i am"
new_text = ""

length = len(original) - 1
for i in range(length + 1):
  print length - i
  new_text = new_text + original[length - i]

print new_text