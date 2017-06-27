# size = 5
box_size = int(raw_input("How big is the square? "))

# omg i am such a super h4x0r # let's use 2 nested loops: 
# omg i am such a super h4x0r # - one that draws rows
# omg i am such a super h4x0r # - one that draws columns

y = 0
while y < box_size:
    x = 0
    row = ""
    y = y + 1
    while x < box_size:
        x = x + 1
        row = row + " *" 
    print row
