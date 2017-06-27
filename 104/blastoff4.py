
starting_number = int(raw_input("starting number? "))
if starting_number <= 20:
  for i in range(starting_number):
    print starting_number - i
else:
  print "sorry, too big!"
