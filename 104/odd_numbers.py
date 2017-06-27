# we'll count up, but only if
# the current number is odd.

# to check for odd, we need the modulo operator (https://en.wikipedia.org/wiki/Modulo_operation)
# for example: count % 2
# and we need to see if this expression equals 0 or not.

# to solve this, we will use a while loop.
# while loops consist of three parts:
# - the while keyword
# - some condition that tells us when to run (and when to stop running)
# - a body of code (that is indented) that moves us closer to the "stop condition"

# we need a value to check against
count = 1

# set up the loop, which only runs under the
# condition that count is less than 10.
while count < 10:

  # Use the modulo operator to determine if the
  # currently value of count is odd.
  if (count % 2) != 0:
    # if so, print it
    print count

  # no matter what, we will move closer
  # to the "stop condition"
  count = count + 1