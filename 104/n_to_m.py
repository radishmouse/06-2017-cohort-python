n = int(raw_input("Start from: "))
m = int(raw_input("End on: "))

# Let's use a while loop.
# Every while loop requires three parts:
# - the while keyword
# - the condition that stops the loop
# - a body of code that moves closer to the "stop condition"

# our loop counts up to a value.

# let's declare a counter variable
# and set the counter to start at n
count = n

# only run if count is less than or equal to the value of m
while count <= m:
    # remember, we have to indent the body of our loop

    # print the current value of count
    print count

    # move us closer to the "stop condition"
    count = count + 1
