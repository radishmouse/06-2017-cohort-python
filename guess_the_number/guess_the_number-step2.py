print('I am thinking of a number between 1 and 10.')
answer = 5
guess = -1 # Give it a dummy value.

while guess != answer:
  guess = int(raw_input('What\'s the number? '))
  if guess < answer:
    print "%d is too low" % guess
  elif guess > answer:
    print "%d is too high" % guess
  else:
    print 'You win!'