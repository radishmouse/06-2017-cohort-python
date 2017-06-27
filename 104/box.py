# size = 5
width = int(raw_input("width? "))
height = int(raw_input("height? "))

brick = " *"
space = "  "

# let's use 2 nested loops: 
# - one that draws rows
# - one that draws columns

# initial value of stop condition for rows
y = 0

# set up loop for drawing rows
while y < height:

    # initial value of stop condition for columns
    x = 0

    # if we're on first or last row
    # just draw a row of asterisks
    if y == 0 or y == (height - 1):
        row = brick * width

    # otherwise, use a while loop to fill out the columns
    else:

        # the row itself starts empty
        row = ""

        # set up the loops
        while x < width:

            # if the current column is one of the sides
            if (x == 0) or (x == (width - 1)):

                # add nother brick for this column
                row = row + brick
            else:

                # add a space for this column
                row = row + space
            
            # move closer to stop condition
            x = x + 1

    # move closer to stop condition
    print row
    y = y + 1
