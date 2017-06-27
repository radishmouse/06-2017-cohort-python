import time

starting_number = int(raw_input("starting number? "))
for i in range(starting_number):
  print starting_number - i
  time.sleep(1)
