# max_height = 4
max_height = int(raw_input("Height? "))
max_width = (max_height * 2) - 1

blanks_to_the_left = max_height - 1
blanks_to_the_right = max_height - 1

height_count = 0
while height_count < max_height:
    height_count = height_count + 1    


    column_count = 1
    row = ""
    while column_count <= max_width:

        if column_count <= blanks_to_the_left:
            row = row + " "
        elif column_count > (max_width - blanks_to_the_right):
            row = row + " "
        else:
            # row = row + str(column_count)
            row = row + "*"

        column_count = column_count + 1

    blanks_to_the_left = blanks_to_the_left - 1
    blanks_to_the_right = blanks_to_the_right - 1
    
    print row